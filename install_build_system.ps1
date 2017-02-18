$build_system_dest="$env:APPDATA\Sublime Text 3\Packages\User"
$build_system_fullpath="$dest\pymake.sublime-build"
$build_cmd="$PSScriptRoot\run_me.bat" -replace "\\", "/"

# COPY SUBLIME TEXT BUILD SYSTEM FILE
$build_json=
"{
    ""cmd"": [""$build_cmd"", ""`$file""]
}"
Write-Host ("save: `n{0} `nto:`n{1}`n" -f $build_json, $build_system_fullpath)
New-Item $build_system_fullpath -ItemType File -Force -Value $build_json





