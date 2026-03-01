-- 1 . Market Trends --

select 
	  year,
	  quarter,
	  micro_market,
	  count(transaction_type) as booking_count 
from luxury_housing_sales_data
where transaction_type = 'Primary'
group by year,quarter,micro_market
order by year,quarter;

-- 2 . Builder Performance --

select developer_name,
	   sum(ticket_price_cr) as aggregated_price_in_cr,
	   avg(ticket_price_cr) as average_in_cr
from luxury_housing_sales_data
where transaction_type = 'Primary'
group by developer_name
order by avg(ticket_price_cr) desc;


-- 3 . Booking Conversion --

select micro_market,
       count(*) as conversions 
from luxury_housing_sales_data
where transaction_type = 'Primary'
group by micro_market
order by count(transaction_type) desc;

-- 4 . Configuration Demand --

select configuration,
       count(configuration) as total 
from luxury_housing_sales_data
group by configuration
order by count(configuration) desc;


-- 5 . Sales Channel Efficiency --

select sales_channel,
       count(*) as conversions 
from luxury_housing_sales_data
where transaction_type = 'Primary'
group by sales_channel
order by count(transaction_type) desc


-- 6 . Top 5 Performers --

select developer_name,
       sum(ticket_price_cr) as revenue,
	   count(*) as total_units_sold 
from luxury_housing_sales_data
where transaction_type = 'Primary'
group by developer_name
order by sum(ticket_price_cr) desc
limit 5;
	   
-- 7 . Infrastructure vs Pricing --

select distinct(floor(locality_infra_score)) as locality_score,
       round(avg(ticket_price_cr)::numeric,2) as avg_ticket_price_cr
from luxury_housing_sales_data
group by distinct(floor(locality_infra_score))
order by score;


-- 8 . Amenity Impact Analysis --

select distinct(floor(amenity_score)) as amenity_scores,
       round(avg(ticket_price_cr)::numeric,2) as avg_ticket_price_cr
from luxury_housing_sales_data
group by distinct(floor(amenity_score))
order by amenity_scores;	

-- 9 . Traffic Impact on Demand --

SELECT
    CASE
        WHEN avg_traffic_time_min <= 40 THEN 'Low Traffic'
        WHEN avg_traffic_time_min <= 80 THEN 'Medium Traffic'
        ELSE 'High Traffic'
    END AS traffic_category,
    COUNT(*) AS booking_volume
FROM luxury_housing_sales_data
WHERE transaction_type = 'Primary'
GROUP BY traffic_category
ORDER BY booking_volume DESC;
