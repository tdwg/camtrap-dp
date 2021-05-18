---
background: /assets/home.jpg
permalink: /
---

# Camera Trap Data Package

**Camera Trap Data Package** (or **Camtrap DP** for short) is a community developed data exchange format for camera trap data. A Camtrap DP is a [Frictionless Data Package](https://frictionlessdata.io/data-package/) that consists of:

File | Description
--- | ---
`datapackage.json`{: .d-inline-block style="width:150px;"} | [Metadata](https://tdwg.github.io/camtrap-dp/metadata/) regarding the data package and camera trap project.
`deployments.csv` | Table with camera trap [deployments](https://tdwg.github.io/camtrap-dp/data/#deployments).
`multimedia.csv` | Table with [multimedia](https://tdwg.github.io/camtrap-dp/data/#multimedia) files captured by the camera traps.
`observations.csv` | Table with [observations](https://tdwg.github.io/camtrap-dp/data/#observations) based on the multimedia files.

See [website](https://tdwg.github.io/camtrap-dp/) for documentation.

## Example

[Example Camtrap DP](https://github.com/tdwg/dwc-for-biologging/tree/403f57db105982dc05b70f3cf66fd2b5591798db/derived/camtrap-dp/data/raw)

## Validation

By building upon Frictionless Data specifications, a Camtrap DP can be validated with:

```shell
pip install frictionless
frictionless validate path/to/your/datapackage.json
```

## Contribute

Want to get involved in the development of Camtrap DP? Watch [the repository](https://github.com/tdwg/camtrap-dp) to get notifications and participate in [issue discussions](https://github.com/tdwg/camtrap-dp/issues).

## Recommended citation

> Camtrap DP Development Team (2021) Camera Trap Data Package <https://github.com/tdwg/camtrap-dp>

Camtrap DP is managed by the [Machine Observations Interest Group](https://www.tdwg.org/community/mobs/) of Biodiversity Information Standards (TDWG). It was originally developed by the [Open Science Conservation Fund](https://os-conservation.org/) and the [Research Institute for Nature and Forest (INBO)](https://inbo.be/en).
