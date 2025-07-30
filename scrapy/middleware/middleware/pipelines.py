from itemadapter import ItemAdapter

class DataPipelinesPipeline:
    def process_item(self, item, spider):
        return item

class QuotesPipeline:
    def process_item(self, item, spider):
        item['text'] = item['text'].strip().replace('"', "'")
        return item

class MiddlewareDemoPipeline:
    def process_item(self, item, spider):
        return item
