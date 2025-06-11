---
title: Changelog
permalink: /changelog/
toc: true
---

## Camtrap DP (development version)

##### Documentation

- The website now has a [Changelog section](https://camtrap-dp.tdwg.org/changelog/) (inspired by [NEWS.md](https://inbo.github.io/camtrapdp/news/index.html) in R packages), so developers have an overview of upcoming changes and previous releases ([#410](https://github.com/tdwg/camtrap-dp/issues/410)).

## Camtrap DP 1.0.2

{:.text-muted}
[Release 1.0.2](https://github.com/tdwg/camtrap-dp/releases/tag/1.0.2) - Release date: 2025-06-10

Patch release to support Parquet data files. No changes are made to the standard (meta)data terms. There is no need to update your implementations or datasets.

The main changes are listed below ([full diff here](https://github.com/tdwg/camtrap-dp/compare/1.0.1...1.0.2)).

##### Package

- `resources` is a required property in Data Package, but is now also defined as such in Camtrap DP, so this is clearer on the website ([#387](https://github.com/tdwg/camtrap-dp/pull/387)).
- The table schemas now include `NA`, `NaN` and `nan` in addition to `""` as allowed `missingValues` in support of Parquet data files ([#408](https://github.com/tdwg/camtrap-dp/pull/408)).

###### Example dataset

- The example dataset now refers to the R package `camtrapdp` rather than `camtraptor` as related resource ([#407](https://github.com/tdwg/camtrap-dp/pull/407)).

##### Documentation

- The website now has a [FAQ section](https://camtrap-dp.tdwg.org/faq/) ([#329](https://github.com/tdwg/camtrap-dp/issues/329)).
- `CITATION.cff` now includes keywords ([#386](https://github.com/tdwg/camtrap-dp/pull/386)).

## Camtrap DP 1.0.1

{:.text-muted}
[Release 1.0.1](https://github.com/tdwg/camtrap-dp/releases/tag/1.0.1) - Release date: 2024-08-21

Patch release to support validation with frictionless-py 5.17 and up. No changes are made the standard (meta)data terms. There is no need to update your implementations or datasets, unless you want to validate Camtrap DPs with the latest version of frictionless-py.

The main changes are listed below ([full diff here](https://github.com/tdwg/camtrap-dp/compare/1.0...1.0.1)).

##### Package

- Fix issue (missing first slash in `"$ref": "#/$defs/version"`) preventing validation with frictionless-py 5.17 and up ([#383](https://github.com/tdwg/camtrap-dp/pull/383)).
- Link to canonical `https://specs.frictionlessdata.io/schemas/data-package.json` ([#384](https://github.com/tdwg/camtrap-dp/pull/384)).
- Use full URL (`https://camtrap-dp.tdwg.org/data`) to point to data page ([#368](https://github.com/tdwg/camtrap-dp/pull/368)).

##### Documentation

- Example dataset's `observations.csv` no longer starts with BOM character and `datapackage.json` no longer contains superfluous `spatial.bbox`([#370](https://github.com/tdwg/camtrap-dp/pull/370)).
- Update README, homepage and add `CITATION.cff` ([#382](https://github.com/tdwg/camtrap-dp/pull/382)).
- Fix typos in test documentation ([#372](https://github.com/tdwg/camtrap-dp/pull/372)).

## Camtrap DP 1.0

{:.text-muted}
[Release 1.0](https://github.com/tdwg/camtrap-dp/releases/tag/1.0) - Release date: 2023-11-03

First major release of Camtrap DP.

Closes all remaining issues in [milestone 1.0](https://github.com/tdwg/camtrap-dp/milestone/1). The main changes compared to [Camtrap DP 1.0-rc.1](https://github.com/tdwg/camtrap-dp/releases/tag/1.0-rc.1) are listed below ([full diff here](https://github.com/tdwg/camtrap-dp/compare/1.0-rc.1...1.0)). Changes in **bold** have implications for software developers. Thanks to all contributors for getting us to this milestone!

##### Package

- Updated term:`project.samplingDesign` refers to http://rs.tdwg.org/eco/terms/inventoryTypes (#351)
- **Updated term**: `project.captureMethod` has a renamed enum value `activityDetection` (from `motionDetection`) ([#361](https://github.com/tdwg/camtrap-dp/pull/361))
- **Deleted term**: `taxonomic.taxonIDReference` ([#363](https://github.com/tdwg/camtrap-dp/pull/363))
- **Updated term**: `taxonomic.taxonID` is no longer required and appears after `scientificName` ([#363](https://github.com/tdwg/camtrap-dp/pull/363))

##### Deployments

- Table description updated to mention "camera placements"
- Updated term: `setupBy` refers to http://rs.tdwg.org/eco/terms/samplingPerformedBy ([#351](https://github.com/tdwg/camtrap-dp/pull/351))
- Updated term: `cameraDelay` no longer mentions the word "trigger" ([#360](https://github.com/tdwg/camtrap-dp/pull/360))
- Updated term: `cameraHeight` refers to http://rs.tdwg.org/dwc/terms/minimumDistanceAboveSurfaceInMeters and http://rs.tdwg.org/dwc/terms/maximumDistanceAboveSurfaceInMeters ([#362](https://github.com/tdwg/camtrap-dp/pull/362))
- **New term**: `cameraDepth` for marine setups, refers to http://rs.tdwg.org/dwc/terms/minimumDepthInMeters and http://rs.tdwg.org/dwc/terms/maximumDepthInMeters ([#362](https://github.com/tdwg/camtrap-dp/pull/362))

##### Media

- Table description rephrased
- **Updated term**: `captureMethod` has a renamed enum value `activityDetection` (from `motionDetection`) ([#361](https://github.com/tdwg/camtrap-dp/pull/361))
- Updated term: `filePublic` refers to http://rs.tdwg.org/ac/terms/serviceExpectation ([#350](https://github.com/tdwg/camtrap-dp/pull/350))
- **Updated term**: `fileMediatype` refers to http://purl.org/dc/elements/1.1/format and expects values to be a IANA Media Type that starts with `image`, `video`, or `audio` ([#350](https://github.com/tdwg/camtrap-dp/pull/350))
- Updated term: `exifData` has file type `any` to allow string representation of json in csv ([#326](https://github.com/tdwg/camtrap-dp/pull/326))

##### Observations

- Table description updated to fix typo
- Updated term: `observationType` mentions the term `classificationProbability` for `unknown` values.
- **Deleted term**: `taxonID` ([#363](https://github.com/tdwg/camtrap-dp/pull/363))

##### Documentation

- **New website URL**: https://camtrap-dp.tdwg.org (https://tdwg.github.io/camtrap-dp will automatically redirect) ([#342](https://github.com/tdwg/camtrap-dp/pull/342))
- Example dataset has at least one value for all columns (except for `deployments.cameraDepth` and `observations.individual*` columns) ([#326](https://github.com/tdwg/camtrap-dp/pull/326))
- Example dataset includes some local media files ([#348](https://github.com/tdwg/camtrap-dp/pull/348))
- Example dataset is documented with [landing page](https://camtrap-dp.tdwg.org/example/) ([#334](https://github.com/tdwg/camtrap-dp/pull/334)) 

---

For pre-releases, see <https://github.com/tdwg/camtrap-dp/releases>.
