#!/usr/bin/env python3
"""
Split novel text file into individual chapter files (chines_chapters/novel_name_XXX.md)

Usage:
    python3 split_chapters.py --input data_file/古道仙鸿.txt
    python3 split_chapters.py --input data_file/古道仙鸿.txt --output chines_chapters
"""

import re
import argparse
import os
from pathlib import Path
from typing import List, Tuple, Dict


def parse_split_config(config_path: str) -> Dict[str, str]:
    """Parse split_title.txt to get custom chapter markers for each novel."""
    if not os.path.exists(config_path):
        return {}
    
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    markers = {}
    # Split by novel_name:
    parts = re.split(r'novel_name:\s*', content)
    for part in parts:
        if not part.strip():
            continue
        
        # Split novel name from the rest
        lines = part.split('\n', 1)
        name = lines[0].strip()
        rest = lines[1] if len(lines) > 1 else ""
        
        # Look for chapter_title:
        # Handles both "title" and """title""" formats
        match = re.search(r'chapter_title:\s*("""(.*?)"""|"(.*?)")', rest, re.DOTALL)
        if match:
            marker = match.group(2) or match.group(3)
            if marker:
                markers[name] = marker.strip()
    
    return markers


def detect_chapter_markers(text: str, custom_marker: str = None) -> List[Tuple[int, str]]:
    """Detect chapter markers in Chinese novel text."""
    if custom_marker:
        markers = []
        start = 0
        while True:
            idx = text.find(custom_marker, start)
            if idx == -1:
                break
            
            # Find which line number this is
            line_num = text.count('\n', 0, idx)
            # Use the first line of the marker as the title
            title_lines = custom_marker.split('\n')
            # If the marker is multiline, try to find a meaningful title in it or use the first non-empty line
            title = next((l.strip() for l in title_lines if l.strip() and '=' not in l), title_lines[0].strip())
            if not title:
                title = f"Chapter {len(markers) + 1}"
            
            markers.append((line_num, title))
            start = idx + len(custom_marker)
        
        if markers:
            print(f"Using custom marker: {repr(custom_marker[:20])}...")
            return markers

    # Common patterns: 第001章, 第一章, 第1章, etc.
    patterns = [
        r'^第\s*[\d零一二三四五六七八九十百千]+\s*章.*$',  # 第001章, 第一章
        r'^Chapter\s+\d+.*$',  # Chapter 1 (English)
    ]
    
    lines = text.split('\n')
    chapters = []
    
    for i, line in enumerate(lines):
        for pattern in patterns:
            if re.match(pattern, line.strip(), re.IGNORECASE):
                chapters.append((i, line.strip()))
                break
    
    return chapters


def split_novel_to_chapters(input_file: str, output_dir: str = "chinese_chapters", config_file: str = "split_title.txt", start_ch: int = 1, end_ch: int = None) -> List[Path]:
    """
    Split novel into individual chapter files.
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Novel file not found: {input_file}")
    
    novel_name = input_path.stem
    chapters_dir = Path(output_dir) / novel_name
    chapters_dir.mkdir(parents=True, exist_ok=True)
    
    # Read novel
    print(f"Reading: {input_file}")
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Load custom markers
    custom_markers = parse_split_config(config_file)
    custom_marker = custom_markers.get(novel_name)
    
    # Find all chapter markers
    chapter_markers = detect_chapter_markers(content, custom_marker)
    
    if not chapter_markers:
        print("No chapter markers found. Treating entire file as single chapter.")
        chapter_markers = [(0, f"第001章 {novel_name}")]
    
    total_found = len(chapter_markers)
    print(f"Found {total_found} chapters")
    
    # Filter chapters if range is provided
    if end_ch is None:
        end_ch = total_found
    
    start_idx = max(0, start_ch - 1)
    end_idx = min(total_found, end_ch)
    
    if start_idx >= total_found:
        print(f"Start chapter {start_ch} is greater than total chapters {total_found}")
        return []

    chapter_markers_to_process = chapter_markers[start_idx:end_idx]
    print(f"Processing chapters {start_idx + 1} to {end_idx}")

    # Split content by chapters
    lines = content.split('\n')
    saved_files = []
    
    for relative_idx, (start_line, chapter_title) in enumerate(chapter_markers_to_process):
        absolute_idx = start_idx + relative_idx
        # Determine end line
        if absolute_idx < len(chapter_markers) - 1:
            end_line = chapter_markers[absolute_idx + 1][0]
        else:
            end_line = len(lines)
        
        # Extract chapter content
        chapter_lines = lines[start_line:end_line]
        chapter_content = '\n'.join(chapter_lines)
        
        # Clean chapter number for filename
        chapter_num = absolute_idx + 1
        
        # Create filename: novel_name_chapter_XXX.md (3 digits)
        filename = f"{novel_name}_chapter_{chapter_num:03d}.md"
        filepath = chapters_dir / filename
        
        # Write chapter file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(chapter_content)
        
        saved_files.append(filepath)
    
    print(f"\n✓ Total: {len(saved_files)} chapters saved to {chapters_dir}/")
    return saved_files


def main():
    parser = argparse.ArgumentParser(
        description="Split novel into chapter files"
    )
    parser.add_argument(
        "--input", "-i",
        default="data_file/古道仙鸿.txt",
        help="Input novel file path"
    )
    parser.add_argument(
        "--output", "-o",
        default="chinese_chapters",
        help="Output directory"
    )
    parser.add_argument(
        "--config", "-c",
        default="split_title.txt",
        help="Config file with custom markers"
    )
    parser.add_argument(
        "--start", "-s",
        type=int,
        default=1,
        help="Starting chapter number"
    )
    parser.add_argument(
        "--end", "-e",
        type=int,
        default=None,
        help="Ending chapter number"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Novel Chapter Splitter")
    print("=" * 60)
    
    try:
        files = split_novel_to_chapters(args.input, args.output, args.config, args.start, args.end)
        print("\n✓ Done!")
        return 0
    except FileNotFoundError as e:
        print(f"\n✗ Error: {e}")
        return 1
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"\n✗ Error: {e}")
        return 1



if __name__ == "__main__":
    exit(main())
