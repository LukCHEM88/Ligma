@echo off
setlocal

set "installDir=%ProgramFiles%\Ligma"
set "resourcesDir=%~dp0Resources"
set "desktopDir=%UserProfile%\Desktop"
set "exeFile=%resourcesDir%\Ligma.exe"
set "iconFile=%resourcesDir%\Icon_Ligma.ico"
set "shortcutFile=%resourcesDir%\Ligma.lnk"

echo Ligma wird installiert...

if not exist "%installDir%" (
    mkdir "%installDir%" || (
        echo Installation fehlgeschlagen. Bitte fuehren sie das Skript als Administrator aus.
        goto :end
    )
)

if not exist "%exeFile%" (
    echo Ligma.exe not found. Installation failed.
    goto :end
)

if not exist "%iconFile%" (
    echo Icon_Ligma.ico not found. Installation failed.
    goto :end
)

copy "%exeFile%" "%installDir%" || (
    echo Failed to copy Ligma.exe. Installation failed.
    goto :end
)

copy "%iconFile%" "%installDir%" || (
    echo Failed to copy Icon_Ligma.ico. Installation failed.
    goto :end
)

echo Desktop Verknuepfung wird erstellt...

copy "%shortcutFile%" "%desktopDir%" || (
    echo Failed to copy Ligma.lnk. Installation failed.
    goto :end
)

echo Installation erfolgreich.
goto :end

:end
pause
