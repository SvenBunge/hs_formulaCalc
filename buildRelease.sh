#!/bin/bash
(cd ../../; python2 ./generator.pyc hs_formulaCalc utf-8)
markdown2 --extras tables,fenced-code-blocks,strike,target-blank-links doc/log14188.md > release/log14188.html
(cd release; zip -r 14188_hs_formulaCalc.hslz *)
