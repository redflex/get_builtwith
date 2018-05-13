# get_builtwith

Get results from builtwith, return b64-encoded json of entire report.

## Building

`docker build -t get_builtwith .`

## Running

The container requires the following environment variables:

| Variable            | Purpose                                               |
|---------------------|-------------------------------------------------------|
| `TARGET_HOST`       | Host name for builtwith query                         |
| `BUILTWITH_TOKEN`   | API key for builtwith.com.                            |

```
docker run \
  -it \
  --rm \
  -e TARGET_HOST=$TARGET_HOST \
  -e BUILTWITH_TOKEN=$BUILTWITH_TOKEN \
  --read-only \
  get_builtwith:latest | base64 -d > ./output.json
```

Note: This tool uses the Python requests library, and not any existing
abstraction or library for builtwith.  The results that come back are exactly
as you would see when performing a `LOOKUP` query against the builtwith json
API.
