# HomeServer Formula Calculator (14188)

Module / LBS for the Gira HomeServer - tested with 4.11
Express your calculation easy with a simple formula. Use math functions and simple logik to express yourself in one module / LBS.

## Developer Notes

Developed for the GIRA HomeServer 4.11 (Could work >4.7)
Licensed under the LGPL to keep all copies & forks free!

:exclamation: **If you fork this project and distribute the module by your own CHANGE the Logikbaustein-ID because 14188 is only for this one and registered to @SvenBunge !!** :exclamation:

If something doesn't work like expected: Just open an issue. Even better: Fix the issue and fill a pull request.

## Installation

Download a [release](https://github.com/SvenBunge/hs_formulaCalc/releases) and install the module / Logikbaustein like others in Experte.
You find the module in the category "Math. Funktionen". 

The latest version of the module is also available in the [KNX-User Forum Download Section](https://service.knx-user-forum.de/?comm=download&id=14188)

## Documentation

For a more [detailed documentation](doc/log14188.md) press F1 by having the LBS marked in Experte.

For further questions use the [Promotion Thread](https://knx-user-forum.de/forum/%C3%B6ffentlicher-bereich/knx-eib-forum/1782168-neuer-formel-baustein-wenn-ihn-jemand-braucht) of the KNX User Forum (German)

## Build from scratch

1. Download [Schnittstelleninformation](http://www.hs-help.net/hshelp/gira/other_documentation/Schnittstelleninformationen.zip) from GIRA Homepage
2. Decompress zip, use `HSL SDK/2-0/framework` Folder for development.
3. Checkout this repo to the `projects/hs_formulaCalc` folder
4. Run the generator.pyc (`python2 ./generator.pyc hs_formulaCalc`)
5. Import the module `release/14188_hs_formulaCalc.hsl` into the Experte Software
6. Use the module in your logic editor

You can replace step 4 with the `./buildRelease.sh` script. With the help of the markdown2 python module (`pip install markdown2`) it creates the documentation and packages the `.hslz` file. This file is also installable in step 5 and adds the module documentation into the Experte-Tool.  
 
## Libraries

Only shipped libraries. Like the `math` library
