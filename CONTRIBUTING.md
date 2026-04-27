# Contributing

## Scope

EarthCapture is intended to stay small and practical:

- keep Google Earth Pro automation focused on extraction tasks
- keep QGIS helpers lightweight and separate from the automation path
- prefer improving configurability and documentation over adding large frameworks

## Development Notes

- test UI automation changes carefully because they are environment-dependent
- keep paths portable and avoid machine-specific absolute paths
- do not commit generated imagery, logs, or large output folders

## Pull Requests

Before opening a pull request:

1. Update documentation when behavior or setup changes.
2. Run a syntax check for edited Python files.
3. Keep changes scoped to one concern where possible.
