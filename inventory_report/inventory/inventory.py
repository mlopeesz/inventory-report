import csv
import json
import xml.etree.ElementTree as ElementTree
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def csv_reader(cls, path):
        inventory = []
        with open(path, encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in data:
                inventory.append(row)
        return inventory

    @classmethod
    def json_reader(cls, path):
        with open(path) as file:
            inventory = json.load(file)
        return inventory

    @classmethod
    def xml_reader(cls, path):
        root = ElementTree.parse(path).getroot()
        inventory = [
            {element.tag: element.text for element in document}
            for document in root
        ]
        return inventory

    @classmethod
    def import_data(cls, path, type):
        inventory = []
        if path.endswith("csv"):
            inventory = Inventory.csv_reader(path)
        elif path.endswith("json"):
            inventory = Inventory.json_reader(path)
        elif path.endswith("xml"):
            inventory = Inventory.xml_reader(path)
        if type == "simples":
            return SimpleReport.generate(inventory)
        else:
            return CompleteReport.generate(inventory)
