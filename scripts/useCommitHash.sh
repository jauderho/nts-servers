#!/bin/bash
#
# Convert select existing GitHub Actions to use commit hashes
#
# Run this at the base directory of your repo
# Make sure to configure .github/dependabot.yml to update "github-actions" in a timely manner
# This may break your setup. Read carefully before running
#
set -euo pipefail
IFS=$'\n\t'

# make sure we have the latest commits
git pull

# initial conversion to commit hashes
sed -i -e 's/docker\/login-action@.*/docker\/login-action@42d299face0c5c43a0487c477f595ac9cf22f1a7/' \
	-e 's/docker\/metadata-action@.*/docker\/metadata-action@e5622373a38e60fb6d795a4421e56882f2d7a681/' \
	-e 's/docker\/setup-buildx-action@.*/docker\/setup-buildx-action@94ab11c41e45d028884a99163086648e898eed25/' \
	-e 's/docker\/setup-qemu-action@.*/docker\/setup-qemu-action@27d0a4f181a40b142cce983c5393082c365d1480/' \
	-e 's/actions\/checkout@.*/actions\/checkout@ec3a7ce113134d7a93b817d10a8272cb61118579/'  \
	-e 's/github\/codeql-action\/upload-sarif@.*/github\/codeql-action\/upload-sarif@1a927e9307bc11970b2c679922ebc4d03a5bd980/' \
	-e 's/anchore\/scan-action@.*/anchore\/scan-action@0001ba0daf81f40441d7f7f0413af69ed10f44b6/' \
	-e 's/actions\/cache@.*/actions\/cache@c64c572235d810460d0d6876e9c705ad5002b353/' \
	-e 's/hendrikmuhs\/ccache-action@.*/hendrikmuhs\/ccache-action@37bc3a8bd27f1cfdc47fe51472b1a6f82ad1ace0/' \
	-e 's/aquasecurity\/trivy-action@.*/aquasecurity\/trivy-action@a7a829a4345428ddd92ca57b18257440f6a18c90/' \
	-e 's/snyk\/actions\/docker@.*/snyk\/actions\/docker@d1ee3d73c6f24375d0efc597c74570b0cd08a323/' \
	.github/workflows/*.yml

# bulk updates (2nd pass)
sed -i -e 's/docker\/build-push-action@ac9327eae2b366085ac7f6a2d02df8aa8ead720a/docker\/build-push-action@e551b19e49efd4e98792db7592c17c09b89db8d8/' \
	-e 's/docker\/login-action@dd4fa0671be5250ee6f50aedf4cb05514abda2c7/docker\/login-action@49ed152c8eca782a232dede0303416e8f356c37b/' \
	-e 's/docker\/metadata-action@b2391d37b4157fa4aa2e118d643f417910ff3242/docker\/metadata-action@69f6fc9d46f2f8bf0d5491e4aabe0bb8c6a4678a/' \
	-e 's/docker\/setup-buildx-action@f211e3e9ded2d9377c8cadc4489a4e38014bc4c9/docker\/setup-buildx-action@dc7b9719a96d48369863986a06765841d7ea23f6/' \
	-e 's/docker\/setup-qemu-action@27d0a4f181a40b142cce983c5393082c365d1480/docker\/setup-qemu-action@8b122486cedac8393e77aa9734c3528886e4a1a8/' \
	.github/workflows/*.yml

# stage the files for commit
git add .github/workflows/*.yml
