#!/usr/bin/env python3
""" manipulate YAML """


import yaml

def main():
    # some data
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
            {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    with open("galaxyguide.yaml", "w") as zfile:
        yaml.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()
