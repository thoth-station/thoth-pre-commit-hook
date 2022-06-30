# Thoth pre-commit hook

Get Thoth advise on your dependencies with the Thoth pre-commit hook.

## Usage

Example usage in `.pre-commit-config.yaml`:

```
---
repos:
  - repo: https://github.com/thoth-station/thoth-pre-commit-hook
    rev: v0.1.2
    hooks:
      - id: thoth-pre-commit-hook
        args: ["--recommendation-type", "security"]
```

The list of arguments that can be specified can be found by running [Thamos](https://pypi.org/project/thamos/), the command line interface to communicate with Thoth's backend:

```
 Usage: thamos advise [OPTIONS]

 Ask Thoth for recommendations on the application stack.
 Ask the remote Thoth service for advise on the application stack used. The command collects information stated in the .thoth.yaml file for the given runtime
 environment, static source code analysis and requirements for the application and sends them to the remote service. Optionally, install packages resolved by Thoth.
 Examples:
 thamos advise --runtime-environment testing --labels 'foo=bar,qux=baz'
 thamos advise --dev
 thamos advise --install
 thamos advise --no-static-analysis --no-user-stack

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│  --debug                                                        Run analysis in debug mode on Thoth.                                                               │
│  --no-write                        -W                           Do not write results to files, just print them.                                                    │
│  --recommendation-type             -t  RECOMMENDATION_TYPE      Use selected recommendation type, do not load it from Thoth's config file.                         │
│  --no-wait                                                      Do not wait for analysis to finish, just submit it.                                                │
│  --no-user-stack                                                Do not submit lock file with the request, this lock file is normally used as a base for            │
│                                                                 comparision to recommend a better stack than the one used.                                         │
│  --no-static-analysis                                           Do not perform static analysis of source code files.                                               │
│  --json                            -j                           Print output in JSON format.                                                                       │
│  --force                                                        Force analysis run bypassing server-side cache.                                                    │
│  --runtime-environment             -r  NAME                     Specify explicitly runtime environment to get recommendations for; defaults to the first entry in  │
│                                                                 the configuration file.                                                                            │
│  --dev                                                          Consider or do not consider development dependencies during the resolution. [default: no-dev]      │
│  --install                                                      Install dependencies once the advise is done. [default: False]                                     │
│  --write-advised-manifest-changes      FILE                     Write advised manifest changes to a file.                                                          │
│  --labels                          -l  KEY1=VALUE1,KEY2=VALUE2  Labels used to label the request.                                                                  │
│  --help                                                         Show this message and exit.                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

 Check Thamos documentation: https://thoth-station.ninja/docs/developers/thamos
```

- `recommendation-type`: Thoth recommendation type for the dependency resolution. Recommendation types available are:

  `security`
  `stable`
  `latest`
  `performance`
  `testing`

See the [documentation on recommendation types](https://thoth-station.ninja/recommendation-types/) for more details.

- `runtime-environment`: Runtime environment used for dependency analysis. Thoth can analyze your dependencies against different runtime environments:

  `ubi-8-py-3.8`
  `rhel-8-py-3.8`
  `fedora-35-py-3.10`
  `fedora-34-py-3.9`


To be able to run this pre-commit hook, the repository must be configured with a `.thoth.yaml` file as specified in the [Thamos CLI documentation](https://github.com/thoth-station/thamos#using-custom-configuration-file-template).
The Thoth pre-commit hook generates a `.thoth_last_analysis_id` file in the dependency requirements file directory after the resolution. To avoid committing it, add it to your repository `.gitignore` file.
