#!/bin/bash

find_and_execute_metacall() {
    local dir="$1"
    local metacall_file="metacall.json"

    while IFS= read -r -d $'\0' file; do
        if [ "${file##*/}" = "$metacall_file" ]; then
            local dir_path="${file%/*}"
            local scripts=$(jq -r '.scripts[]' "$file")
            if [ -n "$scripts" ]; then
                for script in $scripts; do
                    (cd "$dir_path" && metacall "$script")
                done
                echo "Executed scripts from $dir_path"
            fi
        fi
    done < <(find "$dir" -type f -name "$metacall_file" -print0)
}

# Call the function with the current working directory and recursively search all subdirectories
find_and_execute_metacall "$(pwd)" -type d -exec bash -c 'find_and_execute_metacall "$@"' _ {} +