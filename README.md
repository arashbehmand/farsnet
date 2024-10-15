# FarsNet Python Implementation

This project is a Python implementation of FarsNet, a comprehensive lexical database for the Persian language. The main website for FarsNet is [http://farsnet.nlp.sbu.ac.ir/](http://farsnet.nlp.sbu.ac.ir/). The database used in this project is open-sourced under the CC BY-SA license, and all credit goes to the original creators.

## Installation

You can install the FarsNet Python package from PyPI:

```sh
pip install farsnet
```

## Usage

Here is an example of how to use the FarsNet Python package:

```python
import farsnet

# Example usage of the FarsNet sense service
for sense in farsnet.sense_service.get_senses_by_synset(1):
    print(sense.value)

for sense in farsnet.sense_service.get_senses_by_word("START", "آب"):
    print(sense.value)

for rel in farsnet.sense_service.get_sense_relations_by_id(15273):
    print(rel.type_)
    print(rel.sense1().value)
    print(rel.sense2().value)
```

## License

This project is licensed under the MIT License. The FarsNet database is open-sourced under the CC BY-SA license. All credit for the database goes to the original creators.

## Author

Arash Behmand  
Email: arashbehmand@gmail.com