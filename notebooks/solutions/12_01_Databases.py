Entities:
 - shoe: brand, model, price
 - customer: full name, email, password
 - order: code, date, address

Relations:
 - A customer may place many orders, but one order belongs to one customer only.
 - An order may include multiple shoes, and one shoe may be present in several orders. Attributes: size and color
 
E-R diagram:

    Customer              Order                Shoe
    ===========   ---<   =========   >-----<   =======
     full name            code        size      brand
     email                date        color     model
     password             address     units     price



Tables:
 - Shoe: brand, model, price
 - Customer: full_name, email, password
 - Order: code, date, address
 - Item: size, color, units
 
Keys:
 - Shoe: *brand, *model, price
 - Customer: full_name, *email, password
 - Order: *code, date, address, ~customer_email
 - Item: *size, *color, units, *~shoe_brand, *~shoe_model, *~order_code
 
Relational diagram:

    Customer             Order                     Item                   Shoe
    ===========   ---<   ================   ---<   =============   >---   =======
     full_name           *code                     *size                  *brand
    *email                date                     *color                 *model
     password             address                   units                  price
                         ~customer_email           *~shoe_brand
                                                   *~shoe_model
                                                   *~order_code








%%sql
    SELECT brand, model, price
    FROM shoe
    ORDER BY price ASC
    LIMIT 1





%%sql
    SELECT brand, COUNT(*)
    FROM shoe
    GROUP BY brand






%%sql
    SELECT SUM(units)
    FROM "order"
    JOIN item
      ON "order".code = item.order_code
    WHERE code = 4521




%%sql
    SELECT brand, COUNT(*)
    FROM shoe
    JOIN item
      ON item.shoe_brand = shoe.brand AND item.shoe_model = shoe.model
    GROUP BY shoe.brand




%%sql
    SELECT brand, model, COUNT(*)
    FROM shoe
    JOIN item
      ON item.shoe_brand = shoe.brand AND item.shoe_model = shoe.model
    GROUP BY shoe.brand, shoe.model




%%sql
    SELECT address
    FROM "order"
    JOIN customer
      ON customer.email = "order".customer_email
    WHERE customer.full_name = 'Joan Clarke'
    ORDER BY "order".date DESC
    LIMIT 3


%%sql
    SELECT shoe.brand, shoe.model, item.color, item.size
    FROM customer
    JOIN "order"
      ON customer.email = "order".customer_email
    JOIN item
      ON "order".code = item.order_code
    JOIN shoe
      ON shoe.brand = item.shoe_brand AND shoe.model = item.shoe_model
    WHERE customer.full_name = 'Grace Hopper'










%%sql
    SELECT SUM(shoe.price) AS amount
    FROM customer
    JOIN "order"
      ON customer.email = "order".customer_email
    JOIN item
      ON "order".code = item.order_code
    JOIN shoe
      ON shoe.brand = item.shoe_brand AND shoe.model = item.shoe_model
    WHERE customer.full_name = 'Grace Hopper'










    SELECT id
    FROM galaxy
    WHERE flux_g != NULL







    SELECT id
    FROM galaxy
    WHERE flux_g != NULL
      AND flux_r != NULL
      AND flux_i != NULL
      AND flux_z != NULL
      AND flux_y != NULL



    !!!









    Galaxy          Measure
    ======   ---<   ============
    *id             *~galaxy_id
     ra             *band
     dec             flux





    SELECT galaxy_id
    FROM measure
    WHERE band = 'g'







    SELECT galaxy_id
    FROM measure
    GROUP BY galaxy_id
    HAVING COUNT(flux) = 3






    SELECT galaxy_id
    FROM measure
    GROUP BY galaxy_id
    HAVING COUNT(flux) >= 3







