@echo off
echo Installing your essential coding and gaming software...
echo Please wait. This may take several minutes depending on your internet speed.

winget install --id Oracle.JDK.24 -e --accept-package-agreements --accept-source-agreements


:: Game platforms and tools
winget install --id Valve.Steam -e --accept-package-agreements --accept-source-agreements
winget install --id EpicGames.EpicGamesLauncher -e --accept-package-agreements --accept-source-agreements
winget install --id CPUID.HWMonitor -e --accept-package-agreements --accept-source-agreements
winget install --id MSI.Afterburner -e --accept-package-agreements --accept-source-agreements

:: Coding tools
winget install --id Microsoft.VisualStudioCode -e --accept-package-agreements --accept-source-agreements
winget install --id Microsoft.VisualStudio.2022.Community -e --accept-package-agreements --accept-source-agreements
winget install --id JetBrains.IntelliJIDEA.Community -e --accept-package-agreements --accept-source-agreements
winget install --id Python.Python.3 -e --accept-package-agreements --accept-source-agreements
winget install --id OpenJS.NodeJS -e --accept-package-agreements --accept-source-agreements
winget install --id EclipseAdoptium.Temurin.17.JDK -e --accept-package-agreements --accept-source-agreements
winget install --id Git.Git -e --accept-package-agreements --accept-source-agreements
winget install --id JetBrains.PyCharm.Community -e --accept-package-agreements --accept-source-agreements
winget install --id Apache.NetBeans -e --accept-package-agreements --accept-source-agreements


:: Utilities and productivity


:: chrome, everything, notion, obs studio
winget install --id Google.Chrome -e --accept-package-agreements --accept-source-agreements
winget install --id voidtools.Everything -e --accept-package-agreements --accept-source-agreements
winget install --id Notion.Notion -e --accept-package-agreements --accept-source-agreements
winget install --id OBSProject.OBSStudio -e --accept-package-agreements --accept-source-agreements

::Telegram, Discort, WinRar, 7zip, Vlc
winget install --id Telegram.TelegramDesktop -e --accept-package-agreements --accept-source-agreements
winget install --id Discord.Discord -e --accept-package-agreements --accept-source-agreements
winget install --id RARLab.WinRAR -e --accept-package-agreements --accept-source-agreements
winget install --id 7zip.7zip -e --accept-package-agreements --accept-source-agreements
winget install --id VideoLAN.VLC -e --accept-package-agreements --accept-source-agreements

:: Ventoy, Obsidian, SnappyDriver, Rivatunner, Krita, Nmap, Potplayer
winget install --id Ventoy.Ventoy -e --accept-package-agreements --accept-source-agreements
winget install --id Obsidian.Obsidian -e --accept-package-agreements --accept-source-agreements
winget install --id GlennDelahoy.SnappyDriverInstallerOrigin -e --accept-package-agreements --accept-source-agreements
winget install --id Guru3D.RTSS -e --accept-package-agreements --accept-source-agreements
winget install --id KDE.Krita -e --accept-package-agreements --accept-source-agreements
winget install --id Insecure.Nmap -e --accept-package-agreements --accept-source-agreements
winget install --id Daum.PotPlayer -e --accept-package-agreements --accept-source-agreements

:: ProtonVpn, ProtonPass, Speccy, CCleaner, cpu-z, gpu-z
winget install --id Proton.ProtonVPN -e --accept-package-agreements --accept-source-agreements
winget install --id Proton.ProtonPass -e --accept-package-agreements --accept-source-agreements
winget install --id Piriform.Speccy -e --accept-package-agreements --accept-source-agreements
winget install --id Piriform.CCleaner -e --accept-package-agreements --accept-source-agreements
winget install --id CPUID.CPU-Z -e --accept-package-agreements --accept-source-agreements
winget install --id TechPowerUp.GPU-Z -e --accept-package-agreements --accept-source-agreements

:: Firefox, OSD Studio
winget install --id Mozilla.Firefox -e --accept-package-agreements --accept-source-agreements





::winget install --id Microsoft.PowerToys -e --accept-package-agreements --accept-source-agreements

:: not found package
:: pdf lite, 


echo.
echo All installations finished. Enjoy coding and gaming!
pause
