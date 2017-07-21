delete from result;
delete from source;
delete from task;

insert into source(url, enabled, created_at, updated_at) values('http://www.bally.cn/zh/%E9%80%89%E8%B4%AD%E7%94%B7%E5%A3%AB%E7%B3%BB%E5%88%97/%E9%9E%8B%E5%B1%A5/%E9%9D%B4%E5%AD%90/', True, now(), now());
insert into source(url, enabled, created_at, updated_at) values('http://www.bally.cn/zh/%E9%80%89%E8%B4%AD%E7%94%B7%E5%A3%AB%E7%B3%BB%E5%88%97/%E9%9E%8B%E5%B1%A5/%E9%A9%BE%E9%A9%B6%E9%9E%8B/', True, now(), now());
insert into source(url, enabled, created_at, updated_at) values('https://www.bulgari.com/zh-cn/products.html?root_level=861&product_detail_one=228#', True, now(), now());
insert into source(url, enabled, created_at, updated_at) values('https://www.bulgari.com/zh-cn/products.html?root_level=861&product_detail_one=218', True, now(), now());