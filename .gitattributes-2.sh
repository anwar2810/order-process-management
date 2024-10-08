# Set the default behavior, in case people don't have core.autocrlf set.
* text=auto

# Explicitly declare text files you want to always be normalized and converted
# to native line endings on checkout.
*.c text
*.h text

# Declare files that will always have CRLF line endings on checkout.
*.bat text eol=crlf

# Declare files that will always have LF line endings on checkout.
*.sh text eol=lf
*.csv text eol=lf
*.js text eol=lf

# Denote all files that are truly binary and should not be modified.
*.png binary
*.jpg binary
*.xlsx binary

# Use Git LFS to manage .xlsx files
*.xlsx filter=lfs diff=lfs merge=lfs -text

# Specify additional files to be managed by Git LFS
*.jpg filter=lfs diff=lfs merge=lfs -text
*.mp4 filter=lfs diff=lfs merge=lfs -text
*.psd filter=lfs diff=lfs merge=lfs -text
厨房衛浴成本.xlsx filter=lfs diff=lfs merge=lfs -text
五金工具.xlsx filter=lfs diff=lfs merge=lfs -text

# Specify files that need CRLF line endings
*.rtf text eol=crlf