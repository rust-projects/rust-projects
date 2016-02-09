#!/usr/bin/python3

import re
import toml

class DataProduct:
    def __init__(self, condition, subInstance):
        self.condition = condition
        self.subInstance = subInstance

    #abstract
    def calculateProduct(self, project, condition_result):
        return self.subInstance.calculateProduct(project, condition_result)

class TaskRunner():
    def __init__(self, preexisting_state):
        self.results_cache = preexisting_state
        self.data_sources = data_sources
        
    def product(self, conditionName):
        if condition_name is not in self.results_cache:
            self.results_cache[condition_name] = self.run(conditionName)
        return self.results_cache[condition_name]

    def _run(self, conditionName):
        if conditionName is not in self.data_sources:
            raise Exception('that is not a valid data source')
        data_source=self.data_sources[conditionName]

        #please no circular dependencies... :/
        condition_result = data_source.condition(self)
        if condition_result:
            result = 
        else:
            return False

class WebDatapoint:
    def __init__(self,image_url, data_src, snapshot, is_numeric, relevant_link):
        self.image_url = image_url
        self.data_src = data_src
        self.snapshot = snapshot
        self.is_numeric = is_numeric
        self.relevant_link = relevant_link

class WebDatapointFactory:
    def __init__(self,
                 image_url,
                 data_src,
                 get_snapshot,
                 is_numeric,
                 relevant_link: lambda has, cond: has.cond('toml').development_url):
        self.image_url = image_url
        self.data_src = data_src
        self.get_snapshot = get_snapshot
        self.is_numeric = is_numeric
        self.relevant_link = relevant_link

    def makeDatapoint(self, project_info, condition):
        return FetchableData(
            self.image_url(condition) if self.image_url is not None else None,
            self.data_url(condition) if self.data_url is not None else None,
            self.get_snapshot(condition) if self.get_snapshot is not None else None,
            self.is_numeric,
            self.relevant_link(project_info))

class WebServiceProduct:
    def __init__(self, condition, web_datapoint_factories):
        super(condition, self)
        self.resources = web_datapoint_factories

    def calculateProduct(self, project, condition_result):
        result = {}
        for resourceName in self.resources.keys():
            result[resourceName] = self.resources[resourceName].makeDatapoint(
                project, condition)
        return result        

URL_IMG_SHIELDS_IO='https://img.shields.io'
#ALL_VALUES_TRUE= lambda x:

class CalculationProduct:
    def __init__(self, condition, calculation_lambdas):
        super(condition, self)
        self.calculation_lambdas = calculation_lambdas

    def calculateProduct(self, project, condition_result):
        result = {}
        for calculationName in self.calculation_lambdas.keys():
            result[calculationName] = self.calculation_lambdas[calculationName](condition_result)
        return result
    
tasks = {
    'toml' : CalculationProduct(
        
    ),
    'uses_crates_io' : CalculationProduct(
        condition=lambda has : re.match(re_crates_io,
                                        has.product('toml').crates_url) if not has.cond('toml').crate_url is None else None,
        resources={
            'name': lambda re_match : re_match.group(0)
        }
    ),
    'crates_io': WebServiceProduct(
        condition=lambda has : has.product('uses_crates_io'),
        resources={
            'license' : WebDatapointFactory(
                image_url=lambda crates_data : '{}/crates/l/{}.svg'.format(URL_IMAGE_SHIELDS_IO, crates_data.name),
                data_url=None,
                is_numeric=False,
            ),            
            'downloads' : WebDatapointFactory(
                image_url=lambda p : '{}/crates/d/{}.svg'.format(URL_IMAGE_SHIELDS_IO, crates_data.name),
                data_url=None,
                is_numeric=False,
            )
        ]
    ),
    'uses_github' : CalculationProduct(
        condition=lambda has : re.match(re_github_repo,
                                        has.product('toml').repo_url)
        resources={
            'username': lambda re_match : re_match.group(0),
            'reponame': lambda re_match : re_match.group(0)
        }
    )
    'github' : WebServiceProduct(
        condition=lambda has : has.product('uses_github'),
        resources=[
            WebDatapointFactory(
                name='github_license',
                image_url=lambda github_data : '{}/github/license/{}/{}.svg'.format(
                    URL_IMG_SHIELDS_IO, github_data.username, github_data.reponame),
                data_url=None,
                get_snapshot=None,
                is_numeric=False,
            ),
            WebDatapointFactory(
                name='github_stars',
                image_url=lambda github_data : '{}/github/stars/{}/{}.svg?style=social&label=Stars'.format(
                    URL_IMG_SHIELDS_IO, github_data.username, github_data.reponame),
                data_url=None,
                get_snapshot=None
                is_numeric=False
            )
        ]
    )
}

def getProjectData(self, projectPath):
    with open(projectPath, 'r') as tomlString:
        with toml.loads(tomlString) as conffile:
            self.raw_data = TaskRunner(tasks, { 'toml': conffile }).runAll()
            yield ProjectOutput
                

class Serializer:
    def collect_strings_by_locale(self, list_of_cells):
        strings_by_locale = {}
        for cell in locales_by_cell:
            for locale in cell:
                if ! locale instrings_by_locale:
                    strings_by_locale[locale] = []
                strings_by_locale[locale].add(cell[locale])
        return cells_by_locale
    
#todo escape string content
class MarkdownSerializer(Serializer):
    def __init__(self, fields_to_serialize, localization_map):
        self.fields_to_serialize = fields_to_serialize
        self.localization_map = localization_map
        self.serialized = {}
        for locale in localization_map:
            field_descriptors = []
            for field in fields_to_serialize:
                field_descriptors.add(locale[field])
            self.serialized[locale] = [
                #we use self to make it easy to extend later for different markdown formats.
                self.make_table_row(field_descriptors)
                self.make_table_separator()
            ]
            
    def serializeRow(self, list_of_cells):
        strings_by_locale = collect_strings_by_locale(list_of_cells)
        for locale in self.localization_map:
            self.serialized[locale].add(MarkdownSerializer.make_table_row(strings_by_locale[locale]))
        
    def make_table_row(self, stringList):
        return '| ' + stringList.join('|') + ' |'
    
    def make_cell_for_each_locale(self, obj):
        #todo localization and move more things out of loop.
        cell = {}
        for locale in self.localization_map:
            
            if type(obj) == Datapoint:
                if obj.image_url is not None:
                    cell[locale]= '[![{}]({})]({})'.format(image_alt, obj.image_url, obj.relevant_link)
                elif obj.snapshot is not None:
                    cell[locale]= '[{}]({})'.format(str(obj.snapshot), obj.relevant_link)
                else:
                    cell[locale]='[{}]({})'.format(self.localization_map[locale]['link'], obj.relevant_link)
            else:
                cell[locale]= str(obj)
        return cell
        
    def make_table_separator(self, field_descriptors):
        separator_list = [ '---' for x in field_descriptors ]
        return make_table_row(separator_list)
    
    def complete(self):
        completed = {}
        for locale in self.localization_map:
            completed[locale] = self.serialized[locale].join('\n')
        yield completed
        
#provided as an easily javascript-readable format for flexibility in the webpage.
#even if we're using a static site we can still store this as compressed b64
class JsonSerializer(Serializer):
    def __init__(self, fields_to_serialize, localization_map):
        self.fields_to_serialize = fields_to_serialize
        self.localization_map = localization_map
        self.serialized = {}
        for locale in localization_map:
            field_descriptors = []
            for field in fields_to_serialize:
                field_descriptors.add(locale[field])
            self.serialized[locale] = {
                'headers':field_descriptors,
                'data': []
            }

    def serializeRow(self, stringList):
         strings_by_locale = collect_strings_by_locale(list_of_cells)
        for locale in self.localization_map:
            self.serialized[locale].data.add(strings_by_locale[locale]))

    def make_cell_for_each_locale(self, obj):
        #todo localization and move more things out of loop.
        cell = {}
        for locale in self.localization_map:
            if type(obj) == Datapoint:
                #though locale doesnt affect stored value now, it may in the future.
                cell[locale] = {
                    'image_alt':obj.image_alt,
                    'image_url':obj.image_url,
                    'relevant_link':obj.relevant_link,
                    'snapshot':obj.snapshot,
                    'data_url':obj.data_url
                }
            else:
                cell[locale]= str(obj)
        return cell

    def complete(self):
        completed = {}
        for locale in self.localization_map:
            completed[locale] = self.serialized[locale]
        # i forget if gh-pages static site restriction makes it impossible to fetch outside
        # data like the json on the same server, if it is what we're defaulting to doing here
        # is just providing a single giant json for all locales that will take longer to
        # download but could be stored as a single compressed binary blob in the static page.
        yield Json.serialize(completed)

def main():
# todo, main loop function that finds each toml file, reads it, and in a new thread calls getProjectData(), serializes results, and writes serialized results. Work out bugs. Write some tests.
# add commit count metric? concerned it could be easy to game, but definitely at least something like that, downloading and analyzing the git repo.
    pass

if __name__ == '__main__':
    main()
