import pyodbc
#Insert Data into Database
def OpenConnection():
    try:
        con = pyodbc.connect('Driver={SQL Server};'
                      'Server=SNLSQLDEV;'
                      'Database=dba_new;'
                      'Trusted_Connection=yes;')
    except Exception as exp:
        print(exp)
    return con

def CloseConnection(con):
    try:
        con.close()
    except Exception as exp:
        print(exp)

#
connection = OpenConnection()
cursor = connection.cursor()
try:
        query = """declare @inpKeyObj int = 4010;
declare @relatedobjects table( relobj int);
declare @krqs int;
declare @flag1 int = 0, @flag1_limit int = 15,
	    @flag2 int =0, @flag2_limit int = 15;

select @krqs = keyratioquerystructure  from relatedobjectstructure where keyobject in (@inpKeyObj) and keyratiostructuretype = 10

while @krqs != 1330 and @flag1 <= @flag1_limit
begin
               insert into @relatedobjects select keyrelatedobjects from ratioquerystructure where keyratioquerystructure = @krqs
               select @krqs = keyratioquerystructureparent from ratioquerystructure where keyratioquerystructure = @krqs;
			   set @flag1+=1;
end;

if @flag1 >= @flag1_limit begin
select 'Script failed!! Please check manually..' as Output_Message
return
end;

declare @relobjdata table(keyrelatedobject int, keyobject int, keyobjectrelated int);
insert into @relobjdata select KeyRelatedObjects,KeyObject,keyobjectrelated from relatedobjects 
where keyrelatedobjects in (select relobj from @relatedobjects)

--select * from @relobjdata
declare @startobj int = @inpKeyObj;
declare @kro int = 9999;
declare @resultPath varchar(2000)= '';
set @resultPath +=  cast(@startobj as varchar) +' > '

   select @kro = keyobjectrelated from @relobjdata where keyobject = @startobj or keyobjectrelated = @startobj;  
   print 'kro val'+cast(@kro as varchar) 
   if (select count(1) from @relobjdata where keyobject = @kro)>=1 begin
                  --select @kro =keyobject,@startobj=keyobjectrelated from @relobjdata where  keyobject = @kro 
                  print @startobj
                  print @kro
                  set @resultPath +=  cast(@kro as varchar) + ' > ' 
   end
   else if(select count(1) from @relobjdata where keyobjectrelated = @kro) > 1 begin
                  select @kro =keyobject,@startobj=keyobjectrelated from @relobjdata where  keyobjectrelated = @kro and keyobject != @startobj
                  print @startobj
                  print @kro
                  set @resultPath +=  cast(@startobj as varchar) +' > '+ cast(@kro as varchar) + ' > ' 
   end
   else
                              print('Error')

while @kro!=5290 and @flag2 <= @flag2_limit
begin
   if (select count(1) from @relobjdata where keyobject = @kro and keyobjectrelated != @startobj)=1 begin
                              select @startobj =keyobject,@kro = keyobjectrelated from @relobjdata where  keyobject = @kro and keyobjectrelated != @startobj
                              --print @startobj
                              --set @resultPath +=  cast(@startobj as varchar) +' > '
                              print @kro
                              set @resultPath +=  cast(@kro as varchar) +' > '
   end
   else if  (select count(1) from @relobjdata where keyobjectrelated = @kro and keyobject != @startobj)=1  begin
                              select @startobj =keyobjectrelated,@kro = keyobject from @relobjdata where keyobjectrelated = @kro and keyobject != @startobj
                              --print @startobj
                              --set @resultPath +=  cast(@startobj as varchar) +' > '
                              print @kro
                              set @resultPath +=  cast(@kro as varchar) +' > '
   end
   else
        print 'Error'

set @flag2+=1;
end

if @flag2 >= @flag2_limit begin
select 'Script failed!! Please check manually..' as Output_Message
return
end;

--select 'Success' as Output_Message
select @inpKeyObj as Keyobject,substring(@resultPath,1,len(@resultPath)-1) as SecurityPathway"""
        data = cursor.execute(query)

        for d in data:
            print(d)

except Exception as exp:
    print(exp)

finally:
    CloseConnection(connection)
#End