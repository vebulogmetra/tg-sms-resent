create table expense(id integer primary key,
                     bank varchar(255),
                     summ integer,
                     shop_name text,
                     remains integer,
                     created_at datetime,
                     raw_text: text);
