-- START OF FILE
-- ================================================================================
--
-- ==============================
--
-- HATFIELD HOTEL -- ASSIGNMENT  REF DEF
--
-- ==============================
--

-- TASK TWO - Advance SQL  ( 15 in total )
--
-- PLESE READ THIS DOCUMENT CAREFULLY.
-- -----------------------------------
--
-- BEFORE YOU START you must check you have completed the following:
--  
--  0 Download Hatfield_Hotel_Table_and_Data.sql from CANVAS.
--    It is available from the assignment specification description.
--
--  0 Open the file Hatfield_Hotel_Table_and_Data.sql in SQL Developer and
--    use the Run Script icon (icon with page and small green triangle) or
--    accelerator F5 to run the script.
--    Output may show old versions of tables being removed if run multiple
--    times, before creating clean tables and populating with supplied data.
--    First time through the output should be as follows:
--
--  Dropping Tables ...
--  Create Tables ...
--   ... A2_ROOM_TYPE
--   ... A2_ROOM
--   ... A2_GUEST
--   ... A2_BOOKING
--   ... A2_SHOWING
--   ... A2_EXTRA
--   ... A2_PRICE_LIST
--   ... A2_FIXED_EXTRA
--   ... A2_ADDITIONAL_EXTRA
--   
--  All tables created.
--  
--  Populate Tables ...
--   ... A2_Guest
--   ... A2_Booking
--   ... A2_Room_Type
--   ... A2_Room
--   ... A2_Reservation
--   ... A2_Price_List
--   ... A2_Extra
--   ... A2_Fixed_Extra
--   ... A2_Additional_Extra
--
--     All tables re-created and populated.
--
--
--     PL/SQL procedure successfully completed.
--
--
--  0 Confirm that 9 new tables exist all starting A2_
--	  ( A2_Guest, A2_Booking, A2_Room_Type, A2_Room_Type, A2_Reservation
--      A2_Price_List, A2_Extra, A2_Fixed_Extra, A2_Additional_Extra )
--
--  0 Check each table contains data records in each as follows:
--		SELECT COUNT(*) FROM <table>;
--
--	A2_Guest              37
--  A2_Guide              57
--  A2_Room_Type           4
--  A2_Room               49
--  A2_Reservation       183
--  A2_Price_list       1029
--  A2_Extra              87
--  A2_Fixed_Extra        28
--  A2_Additional_Extra   33
--
--
--  0 Only once you are happy with the tables and data, then progress to the two
--    tasks:


-- QUESTION 1 - Simple view
-- Create a simple VIEW called viewGuest which display all data from A2_GUEST
-- Write your SQL here
CREATE OR REPLACE VIEW viewGuest AS SELECT * FROM A2_GUEST;
-- Solution TEST
-- run script select * from viewGuest
-- Output will be
-- GUEST_ID    FAMILY_NAME   GIVEN_NAME    DATE_OF_BIRTH   ADDRESS
-- 933458	Robbins	Martha	16-APR-92	74b, Sandley Towers, Sandley
-- 226725	Silver	Richard 	09-SEP-65	298, Christchurch Lane, Lindon
-- 632134	Lance	Abe	27-FEB-59	81, Templemead, Sharpenley
-- 038464	Martins	Rebecca	13-SEP-86	34, Mount Drive, Lindon
-- 826367	Grace	Thomas	16-NOV-00	23, High Street, Lindon
-- .... so on
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
-- QUESTION 2 View with Aliases
-- Create a simple view called viewGuestName which displays all guest from A2_GUEST.
-- Your view should display full name, date of birth and address of all guests, order by guests full name.
-- Write your SQL here
CREATE OR REPLACE VIEW viewGuestName AS SELECT FAMILY_NAME || ' ' || GIVEN_NAME AS FULL_NAME,DATE_OF_BIRTH,ADDRESS FROM A2_GUEST ORDER BY FULL_NAME
-- OUTPUT
-- View VIEWGUESTNAME created.
-- Solution TEST
-- RUN SCRIPT 
-- select * from viewGuestName
-- Output will be

-- FULL_NAME     DATE_OF_BIRTH   ADDRESS
-- Amman Said	26-JUL-83	29, The Roost, Cosset
-- Dixon Mel	04-APR-60	41, Highridge Way, Layburn
-- Fellows Aaron	14-DEC-68	12, Abbey Road, Southlands
-- Fellows John	18-DEC-99	18, Whooper Way, Cosset
-- Gaye Anthony	17-JUL-76	31, Priory Walk, Lyndham
-- Genoa Carrie	16-DEC-76	106, Ridgeway, Sharpenley
-- Grace Terence	30-MAY-61	23, High Street, Lindon
-- ... so on
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
--QUESTON 3 VIEW  WITH CONDITION
-- create view named viewGuestFromLindon which displays all guests from LINDON.
-- Write your SQL here
CREATE OR REPLACE VIEW viewGuestFromLindon AS SELECT * FROM A2_GUEST WHERE INSTR(UPPER(ADDRESS), 'LINDON') > 0
-- Solution TEST
-- run script select * from viewGuestFromLindon
-- Output will be
-- GUEST_ID    FAMILY_NAME   GIVEN_NAME    DATE_OF_BIRTH   ADDRESS
-- 226725	Silver	Richard 	09-SEP-65	298, Christchurch Lane, Lindon
-- 038464	Martins	Rebecca	13-SEP-86	34, Mount Drive, Lindon
-- 826367	Grace	Thomas	16-NOV-00	23, High Street, Lindon
-- 082164	Marvin	Leon	08-FEB-89	The Marches, Teal Avenue, Lindon
-- 193445	Strettle	George	01-JAN-84	Rose Cottage, Mount Drive, Lindon
-- 838384	Grace	Terence	30-MAY-61	23, High Street, Lindon
-- 485639	Kline	Kevin	07-JUN-91	43, Sandpit Drive, Lindon
-- 835123	Oslovski	Boris	13-OCT-87	108, High Street, Lindon
-- 874902	Wilson	Claire	16-JUN-97	54, The Greenway, Lindon
-- 180558	Leeman	Terence	17-MAY-95	3, Meadow View, Lindon
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
--QUESTION 4 view from Joint
-- The view should display family name and given name of all guests and the total number of booking they placed, 
-- order by family name and given name.
-- Order in alphabetic order of  family name followed by given name
-- WRITE YOUR SQL HERE
CREATE OR REPLACE VIEW VIEWBOOKINGCOUNT AS SELECT DISTINCT g.FAMILY_NAME,g.GIVEN_NAME,COUNT(b.booking_number) OVER (PARTITION BY b.GUEST ORDER BY b.GUEST) AS BOOKING FROM A2_GUEST g LEFT OUTER JOIN A2_BOOKING b ON g.GUEST_ID = b.GUEST ORDER BY FAMILY_NAME,GIVEN_NAME ASC
-- OUTPUT
-- View VIEWBOOKINGCOUNT created.
---------------------------------------------------------
-- Solution TEST
-- RUN SCRIPT 
-- select * from viewBookingCount
-- OUTPUT will be
-- FAMILY_NAME   GIVEN_NAME  BOOKING
------------------------------------------
-- Amman	Said	1
-- Dixon	Mel	1
-- Fellows	Aaron	2
-- Fellows	John	3
-- Gaye	Anthony	3
-- Genoa	Carrie	2
-- Grace	Terence	0
-- Grace	Thomas	3
-- Holmsworthy	Claire	0
-- Kline	Kevin	0
-- so on...
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
-- QUESTION 5 READ ONLY VIEW
-- Create Read only view viewRoomOnly which display all records from A2_ROOM.
-- Write your SQL here
CREATE OR REPLACE VIEW viewRoomOnly AS SELECT * FROM A2_ROOM WITH read ONLY;

--OUTPUT
-- View VIEWROOMONLY created.
-- Solution TEST
-- RUN SCRIPT
-- insert into viewRoomOnly values (504,'Single','Y','N','N')
-- You will get error
-- Error report -
-- SQL Error: ORA-42399: cannot perform a DML operation on a read-only view
-- 42399.0000 - "cannot perform a DML operation on a read-only view"
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
--QUESTION 6 PL/SQL  BLOCK WITH  CURSOR  
-- Write a PL/SQL block that uses a cursor to list all guests and their addresses who live in High Street.
-- Guest name should have family name and given name.
-- WRITE YOUR PL/SQL block HERE
SET SERVEROUTPUT ON SIZE 30000;

DECLARE 
   family_name A2_GUEST.FAMILY_NAME%type; 
   given_name A2_GUEST.GIVEN_NAME%type; 
   address A2_GUEST.ADDRESS%type; 
  
   CURSOR allguests is 
      SELECT FAMILY_NAME,GIVEN_NAME,ADDRESS FROM A2_GUEST WHERE INSTR(UPPER(ADDRESS), 'HIGH STREET') > 0; 
BEGIN 
   OPEN allguests; 
   LOOP 
   FETCH allguests into family_name,given_name, address;
      EXIT WHEN allguests%notfound; 
      dbms_output.put_line('Guest Name:' || family_name || ' ' || given_name || ' ADDRESS: ' || address ); 
   END LOOP; 
   CLOSE allguests; 
END;
-- OUTPUT
-- PL/SQL procedure successfully completed.
-- Dbms Output
-- Guest Name :Grace Thomas  ADDRESS: 23, High Street, Lindon
-- Guest Name :Grace Terence  ADDRESS: 23, High Street, Lindon
-- Guest Name :Oslovski Boris  ADDRESS: 108, High Street, Lindon
-- Guest Name :Oslovski Boris  ADDRESS: 108, High Street, Lindon
-- PL/SQL procedure successfully completed.
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
-- QUESTION 7 PL/SQL FUNCTION [simple function]
-- Write a PL/SQL function named 'getDiscountPrice' which takes original price and percentage discount as argument and return the discounted price
-- Note: discounted price = original Price * (1-perDiscount)
-- WRITE YOUR PL/SQL block HERE
CREATE OR REPLACE FUNCTION getDiscountPrice(
   original_price IN NUMBER,
   percentage_discount IN NUMBER
)
RETURN NUMBER AS
    discounted_price NUMBER;
BEGIN
    discounted_price := original_price-(original_price*percentage_discount)/100;

    RETURN discounted_price;
END; 
-- OUTPUT
-- Function GETDISCOUNTPRICE compiled
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
-- QUESTION 8 Calling function from SQL Clause
-- call the function 'getDiscountPrice()' defined in question 7 to find the discounted price of the item whose original price was 120 . 
-- 55% discount is applied in the item.
-- Hint: use dual for calling function
-- Write your SQL here
Select getDiscountPrice(120,55) AS DiscountPrice from dual;

-- OUTPUT
-- DISCOUNTPRICE
-- 54
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
-- QUESTION 9 Calling the function inside SQL Clause
-- Write a query that displays the original price and discounted Price of all items from A2_PRICE_List
-- Your query should display ROOM_NUMBER, SEASON, weekday, original price as �oldPrice� and discounted price as �new Price�.
-- Write your SQL here
 SELECT ROOM_NUMBER,SEASON,WEEKDAY,PRICE AS OldPrice, getDiscountPrice(PRICE,20) AS newPrice FROM A2_PRICE_LIST;
-- OUTPUT
-- ROOM_NUMBER SEASON WEEKDAY OldPrice  newPrice
--  001	        Low	    Mon	    75.5	60.4
--  002	        Low	    Mon	    75.5	60.4
--  003     	Low	    Mon	    75.5	60.4
--  004	        Low	    Mon	    75.5	60.4
--  005	        Low	    Mon	    75.5	60.4
--  101	        Low	    Mon	    75.5	60.4
-- ... so on  
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------


    
-- Question 10  PL/SQL FUNCTION [simple function]
-- Create a simple PL/SQL function 'getTotalGuest' that returns total number of guests.
-- Hint: Total Number is guest is the count of items in A2_GUEST
-- WRITE YOUR PL/SQL block HERE
CREATE OR REPLACE FUNCTION getTotalGuest

RETURN NUMBER AS
    totalGuest NUMBER;
BEGIN
    SELECT COUNT(*) INTO totalGuest FROM A2_GUEST;

    RETURN totalGuest;
END; 

-- OUTPUT
-- Function GETTOTALGUEST compiled

-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
-- Question 11 Calling PL/SQL function as normal function
-- Write a PL/SQL block that call the function 'getTotalGuest()' as a normal function
-- Your PL/SQL block should display the total number of guest in the Dbms Output
-- Note:
-- use DBMS_OUTPUT.put_line for display 
-- !! call the function getTotalGuest() inside PL/SQL block not in SQL clause !!
-- WRITE YOUR PL/SQL block HERE
BEGIN 
    dbms_output.put_line('Total Guest :'|| getTotalGuest());
END;

-- OUTPUT
-- PL/SQL procedure successfully completed.
-- Dbms Output
-- Total Guest :38
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
-- QUESTION 12 Simple Tigger
-- Create a trigger named 'displayPriceChange' that displays old price, new price and price difference in Dbms Output whenever price of room (item from A2_PRICE_List) is updated.
-- WRITE YOUR PL/SQL block HERE
CREATE OR REPLACE TRIGGER displayPriceChange
AFTER UPDATE
   ON A2_PRICE_List
   FOR EACH ROW
DECLARE
   oldPrice NUMBER;
   newPrice NUMBER;
   priceDifference NUMBER;
BEGIN
   oldPrice:=:old.price;
   newPrice:=:new.price;
   priceDifference:=newPrice-oldPrice;
   DBMS_OUTPUT.PUT_LINE('Old Price: '|| oldPrice|| chr(10) || 'New Price: '||  newPrice || chr(10) || 'Price Difference: ' || priceDifference);
END;
-- OUTPUT
-- Trigger DISPLAYPRICECHANGE compiled
-- Dbms Output will be
-- Old Price: 100
-- New Price: 120
-- Price difference: 20
-------------------------------------------------------------------------------------------------
DROP TRIGGER displayPriceChange;
-------------------------------------------------------------------------------------------------
-- QUESTION 13 CONDITIONAL TIGGER
-- Write a trigger that overwrite the change in room price if new price is less than previous price
-- Your tigger must displays 'Business ERROR !! you can not decrease room price !!' and alter the change if user tried to decrease room price
-- Write your SQL here
CREATE OR REPLACE TRIGGER stopRecession
FOR UPDATE
   ON A2_PRICE_List
COMPOUND TRIGGER
    oldPrice NUMBER;
    newPrice NUMBER;
    
    roomNumber VARCHAR2(4);
    season VARCHAR2(4);
    weekday CHAR(4);
    
BEFORE STATEMENT IS
BEGIN
    DBMS_OUTPUT.PUT_LINE('');
END BEFORE STATEMENT;
      
BEFORE EACH ROW IS
BEGIN
    DBMS_OUTPUT.PUT_LINE('');
END BEFORE EACH ROW;

AFTER EACH ROW IS
BEGIN
   oldPrice:=:old.price;
   newPrice:=:new.price;
   
   roomNumber:=:old.room_number;
   season:=:old.season;
   weekday:=:old.weekday;
   
END AFTER EACH ROW;

AFTER STATEMENT IS
BEGIN
   IF newPrice<oldPrice THEN
        DBMS_OUTPUT.PUT_LINE('Business ERROR !! you can not decrease room price !!');
        UPDATE A2_PRICE_LIST SET PRICE=oldPrice WHERE ROOM_NUMBER=roomNumber AND SEASON=season AND WEEKDAY=weekday AND price=newPrice;
   END IF; 
END AFTER STATEMENT;

END;

-- OUTPUT
-- Trigger STOPRECESSION compiled
-- Solution Test
-- After the tigger is complied RUN the SQL script below
-- update A2_PRICE_LIST set price = price - 10 where ROOM_NUMBER = '001' and SEASON ='High' and WEEKDAY = 'Mon'
-- Dbms Output
-- Business ERROR !! you can not  decrease room price !!
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
--QUESTION 14 PL/SQL EXCEPTION [ type 1 ]
DECLARE
   vRoomType  A2_ROOM_TYPE%ROWTYPE;
BEGIN
   SELECT * INTO vRoomType FROM A2_ROOM_TYPE WHERE A2_ROOM_TYPE.ROOM_TYPE='Duplex';
   dbms_output.put_line('Number of Sleeps is :'||vRoomType.sleeps);
END;
-- PLSQL block above throws error as:
-- Error report -
-- ORA-01403: no data found
-- ORA-06512: at line 4
-- 01403. 00000 -  "no data found"
-- *Cause:    No data was found from the objects.
-- *Action:   There was no data from the objects which may be due to end of fetch.
-- List the Name of the error

-- Identify the type of the error, and rewrite the PL/SQL block such that the error is traped.
-- Display appropriate error message for the error
-- WRITE YOUR PL/SQL block HERE

DECLARE
   vRoomType  A2_ROOM_TYPE%ROWTYPE;
BEGIN
   SELECT * INTO vRoomType FROM A2_ROOM_TYPE WHERE A2_ROOM_TYPE.ROOM_TYPE='Duplex';
    dbms_output.put_line('Number of Sleeps is :'||vRoomType.sleeps);
   
EXCEPTION
    WHEN NO_DATA_FOUND THEN
         dbms_output.put_line('<< The type of this exception is: The Predefined Exception (NO_DATA_FOUND)  >>');
         
END;

-- OUTPUT
-- PL/SQL procedure successfully completed.
-- Dbms Output
-- << Error message>>


-- Write your SQL here
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
--QUESTION 15 PL/SQL EXCEPTION [type 2]
-- Write your SQL here

DECLARE
   vRoom  A2_ROOM%ROWTYPE;
BEGIN
   SELECT * INTO vRoom FROM A2_ROOM WHERE A2_ROOM.ROOM_TYPE='Family';
   dbms_output.put_line('ROOM_NUMBER  :'||vRoom.ROOM_NUMBER);
END;

-- PL/SQL block above throw the error:
-- Error report -
-- ORA-01422: exact fetch returns more than requested number of rows
-- ORA-06512: at line 4
-- 01422. 00000 -  "exact fetch returns more than requested number of rows"
-- *Cause:    The number specified in exact fetch is less than the rows returned.
-- *Action:   Rewrite the query or change number of rows requested

-- Identify the type of the error, and rewrite the PL/SQL block such that the exception is traped.
-- Display appropriate error message
-- WRITE YOUR PL/SQL block HERE
DECLARE
   vRoom  A2_ROOM%ROWTYPE;
BEGIN
   SELECT * INTO vRoom FROM A2_ROOM WHERE A2_ROOM.ROOM_TYPE='Family';
   dbms_output.put_line('ROOM_NUMBER  :'||vRoom.ROOM_NUMBER);
   
EXCEPTION
    WHEN TOO_MANY_ROWS THEN
         dbms_output.put_line('<< The type of this exception is: The Predefined Exception (TOO_MANY_ROWS)  >>');
END;

-- OUTPUT
-- PL/SQL procedure successfully completed.
-- Dbms Output
-- << Error message>>
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
--END


