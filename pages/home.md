---
title: Camtrap DP
background: /assets/home.jpg
permalink: /
description: Data exchange format for camera trap data
---

**Camera Trap Data Package** (Camtrap DP) is a community-developed data exchange format for camera trap data. A Camtrap DP is a [Frictionless Data Package](https://specs.frictionlessdata.io/data-package/) that consists of:

File | Description
--- | ---
`datapackage.json`{:.d-inline-block style="width:150px;"} | [Metadata](metadata/) about the data package and camera trap project.
`deployments.csv` | Table with camera trap placements ([deployments](data/#deployments)).
`media.csv` | Table with [media](data/#media) files recorded during deployments.
`observations.csv` | Table with [observations](data/#observations) derived from the media files.

## Context

See [Bubnicki et al. (2023)](https://doi.org/10.1002/rse2.374) to learn more about Camtrap DP.

## Example

See the [example dataset](example/).

## Software

- [camtrapdp](https://inbo.github.io/camtrapdp): R package to read and manipulate Camtrap DP.
- [Agouti](https://agouti.eu): Data management platform, uses Camtrap DP as export format.
- [TRAPPER](https://os-conservation.org/projects/trapper): Data management platform, uses Camtrap DP as export format.
- [Integrated Publishing Toolkit (IPT)](https://www.gbif.org/ipt) (v3): Online software tool to publish biodiversity datasets to the Global Biodiversity Information Facility (GBIF). See the [2022 webinar](https://www.gbif.org/composition/4fZGV2vrXjo3rNxySz41sj/exploring-camera-trap-data) for context and [Reyserhove et al. (2023)](https://doi.org/10.35035/doc-0qzp-2x37) for publication guidelines.

## Validation

To allow validation, the `datapackage.json` of your dataset should reference the used version of Camtrap DP, both in `profile` and the resources' `schema`:

```json
{
   "name": "...",
   "profile": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/camtrap-dp-profile.json",
   "resources": [
      {
         "name": "deployments",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/deployments-table-schema.json"
      },
      {
         "name": "media",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/media-table-schema.json"
      },
      {
         "name": "observations",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/observations-table-schema.json"
      }
   ]
}
```

You can validate your dataset against the specifications of Camtrap DP (and Frictionless Data Package) with:

```shell
pip install frictionless
frictionless validate path/to/your/datapackage.json
```

## Contribute

Questions? Suggestions? Contribute to the development of Camtrap DP by watching the [repository](https://github.com/tdwg/camtrap-dp) and participating in [issue discussions](https://github.com/tdwg/camtrap-dp/issues).

## Citation

To cite the Camtrap DP paper:

> Bubnicki JW, Norton B, Baskauf SJ, Bruce T, Cagnacci F, Casaer J, Churski M, Cromsigt JPGM, Farra SD, Fiderer C, Forrester TD, Hendry H, Heurich M, Hofmeester TR, Jansen PA, Kays R, Kuijper DPJ, Liefting Y, Linnell JDC, Luskin MS, Mann C, Milotic T, Newman P, Niedballa J, Oldoni D, Ossi F, Robertson T, Rovero F, Rowcliffe M, Seidenari L, Stachowicz I, Stowell D, Tobler MW, Wieczorek J, Zimmermann F, Desmet P (2023). Camtrap DP: an open standard for the FAIR exchange and archiving of camera trap data. Remote Sensing in Ecology and Conservation. <https://doi.org/10.1002/rse2.374>

To cite the Camtrap DP standard, use the [citation provided by GitHub](https://github.com/tdwg/camtrap-dp), which is generated from a `CITATION.cff` file. See [About CITATION files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) for more info.

Camtrap DP is managed by the [Machine Observations Interest Group](https://www.tdwg.org/community/mobs/) of Biodiversity Information Standards (TDWG).
