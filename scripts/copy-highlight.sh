#!/bin/bash

pygmentize -l py3 -g -f rtf $1 | pbcopy
