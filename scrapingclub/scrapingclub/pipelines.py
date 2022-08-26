from pymongo import MongoClient


# class ScrapingclubPipeline:
#
#     def open_spider(self, spider):
#         self.client = MongoClient('localhost', 27017)
#         self.db = self.client['scrapy_clothes']
#
#     def process_item(self, item, spider):
#         self.db['clothes'].insert_one(item)
#         # return item
#
#     def close_spider(self, spider):
#         self.client.close()


class ScrapingclubPipelineSplash:

    def open_spider(self, spider):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['splash_clothes']

    def process_item(self, item, spider):
        self.db['clothes'].insert_one(item)
        # return item

    def close_spider(self, spider):
        self.client.close()
