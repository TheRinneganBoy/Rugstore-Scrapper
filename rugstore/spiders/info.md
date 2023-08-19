#css selectors

next_page= response.css('a[title=Next]::attr(href)').get()

productname = 

allproducts = > response.css('div.product-item-info')

price = response.css('div.price-box.price-final_price::text').get()

link = response.css('a.product-item-link::attr(href)').get()

title = response.css('img.product-image-photo.image::attr(alt)').get()

 price-box price-final_price
 
 product-item-link

 product-image-photo image