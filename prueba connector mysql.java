import java.sql.*;  
class MysqlCon{  
    public static void main(String args[]){  
        try{  
            Class.forName("com.mysql.jdbc.Driver");  
            Connection con=DriverManager.getConnection(  
            "jdbc:mysql://localhost:3306/sex","root",""); 
            Statement stmt=con.createStatement();  
            ResultSet rs=stmt.executeQuery("select * from persona");  
            while(rs.next())  
            System.out.println(rs.getString(1));  
            con.close();  
        }
        catch(Exception e){ System.out.println(e);}  
    }  
} 
