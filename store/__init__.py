from tortoise import Tortoise, fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator
import asyncio


# 定义一个 Tortoise 模型
class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()


# 创建异步事件循环
async def main():
    # 连接到数据库
    await Tortoise.init(
        db_url='mysql://root:123456@localhost:3306/pixiv_crawler',
        modules={'models': ['__main__']},
    )

    # 生成数据表
    await Tortoise.generate_schemas()

    # 创建一个产品
    product = await Product.create(name='Laptop', description='Powerful laptop for development')

    # 查询所有产品
    products = await Product.all()
    for p in products:
        print(f"Product ID: {p.id}, Name: {p.name}, Description: {p.description}")

    # 查询单个产品
    laptop = await Product.get(name='Laptop')
    print(f"Product ID: {laptop.id}, Name: {laptop.name}, Description: {laptop.description}")

    # 删除产品
    await laptop.delete()

    # 关闭连接
    await Tortoise.close_connections()


# 运行异步事件循环
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
