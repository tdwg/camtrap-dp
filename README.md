# Camera Trap Data Package

**Camera Trap Data Package** (or **Camtrap DP** for short) is a community developed data exchange format for camera trap data. A Camtrap DP is a [Frictionless Data Package](https://frictionlessdata.io/data-package/) that consists of:

File | Description | Documentation
--- | --- | ---
`datapackage.json`<img width=150> | Metadata regarding the data package and camera trap project. | [Docs](https://tdwg.github.io/camtrap-dp/metadata/) / [Specs](https://github.com/tdwg/camtrap-dp/blob/main/camtrap-dp-profile.json)
`deployments.csv` | Table with camera trap deployments. | [Docs](https://tdwg.github.io/camtrap-dp/tables/#deployments) / [Specs](https://github.com/tdwg/camtrap-dp/blob/main/deployments-table-schema.json)
`multimedia.csv` | Table with multimedia files captured by the camera traps. | [Docs](https://tdwg.github.io/camtrap-dp/tables/#multimedia) / [Specs](https://github.com/tdwg/camtrap-dp/blob/main/multimedia-table-schema.json)
`observations.csv` | Table with observations based on the multimedia files. | [Docs](https://tdwg.github.io/camtrap-dp/tables/#observations) / [Specs](https://github.com/tdwg/camtrap-dp/blob/main/observations-table-schema.json)

## Documentation

See [website](http://tdwg.github.io/camtrap-dp).

## Example

[Example Camtrap DP](https://github.com/tdwg/dwc-for-biologging/tree/403f57db105982dc05b70f3cf66fd2b5591798db/derived/camtrap-dp/data/raw)

## Validation

By building upon Frictionless Data specifications, a Camtrap DP can be validated with:

```shell
pip install frictionless
frictionless validate path/to/your/datapackage.json
```

## Contribute

You can contribute by watching [the repository](https://github.com/tdwg/camtrap-dp) and participating in the [issue discussions](https://github.com/tdwg/camtrap-dp/issues).

## Recommended citation

> Camtrap DP Development Team (2021) Camera Trap Data Package <https://github.com/tdwg/camtrap-dp>
