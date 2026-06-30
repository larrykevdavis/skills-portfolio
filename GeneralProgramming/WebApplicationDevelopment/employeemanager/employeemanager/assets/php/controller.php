<?php  
session_start();

// Function to initiate connection to the database
function createConnection(){
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "employeemanager";

	// Create connection
	$connection = new mysqli($servername, $username, $password, $dbname);

	// Check connection
	if ($connection->connect_error) {
	  die("Connection failed: " . $connection->connect_error);
	}

	return $connection;
}

// function to add a user to the database through prepared insert query
function createUser($email,$password){
	$result="";

	$connection=createConnection();

	$createUserQuery = $connection->prepare("INSERT INTO user (email, password) VALUES (?, ?)");
	$passHash = password_hash($password, PASSWORD_DEFAULT);
	$createUserQuery->bind_param("ss", $email, $passHash);
	$result=$createUserQuery->execute();

	$createUserQuery->close();
	$connection->close();

	return $result;
}


// function to read a user from the database
function readUser($email){
	$connection=createConnection();
	$employeeID=0;

	$readUserQuery = $connection->prepare("SELECT employeeID FROM user WHERE email=?");
	$readUserQuery->bind_param("s", $email);
	$readUserQuery->execute();

	$result = $readUserQuery->get_result();

	while ($row = $result->fetch_assoc()) {
	    $employeeID=$row["employeeID"];
	}

	$readUserQuery->close();
	$connection->close();

	return $employeeID;
}

// function to delete user
function deleteUser($email){
	$connection=createConnection();
	$employeeID=0;

	$deleteUserQuery = $connection->prepare("DELETE FROM user WHERE email=?");
	$deleteUserQuery->bind_param("s", $email);
	$deleteUserQuery->execute();

	$deleteUserQuery->close();
	$connection->close();

	return $employeeID;
}

// function to add an employee information to the database
function register($email,$password,$employeeName,$age,$location){
	$status=0;

	$connection=createConnection();

	$result=createUser($email,$password);


	if($result){
		$employeeID=readUser($email);

		$registerQuery = $connection->prepare("INSERT INTO employee (employeeID,employeeName,age,location) VALUES (?, ?,?,?)");
		$registerQuery->bind_param("isis", $employeeID, $employeeName,$age,$location);
		$result=$registerQuery->execute();

		if($result){
			$status=1;
		}

		$registerQuery->close();
	}

	$connection->close();

	return $status;
}

// function for authenticating a user.
function login($email,$password){
	$status=0;
	$connection=createConnection();

	$loginQuery = $connection->prepare("SELECT * FROM user WHERE email=?");
	$loginQuery->bind_param("s", $email);
	$loginQuery->execute();

	$result = $loginQuery->get_result();

	while ($row = $result->fetch_assoc()) {
		$passHash=$row["password"];
		$role=$row["role"];

		$_SESSION["email"]=$row["email"];
		$_SESSION["employeeID"]=$row["employeeID"];
		

		if(password_verify($password, $passHash)) {
			if($role==0){
				header("location:../");
			}else if($role==1){
				header("location:../admin");
			}
		}else{
			$_SESSION['login_err']="Invalid Username or Password. Try Again!";
		}
	}

	$loginQuery->close();
	$connection->close();

	return $status;

}

// function for reading the profile information of an employee
function readProfile($employeeID){
	$connection=createConnection();
	
	$readProfileQuery = $connection->prepare("SELECT * FROM employee WHERE employeeID=?");
	$readProfileQuery->bind_param("s", $employeeID);
	$readProfileQuery->execute();

	$result = $readProfileQuery->get_result();

	while ($row = $result->fetch_assoc()) {
	    $_SESSION['employeeName']=$row["employeeName"];
	    $_SESSION['age']=$row["age"];
	    $_SESSION['location']=$row["location"];
	    $_SESSION['qualifications']=$row["qualifications"];
	    $_SESSION['jobTitle']=$row["jobTitle"];
	}

	$readProfileQuery->close();
	$connection->close();
}

// function for updating the fprofile information
function updateProfile($employeeID,$employeeName,$age,$location,$qualifications){
	$status=0;

	$connection=createConnection();
	
	$updateProfileQuery = $connection->prepare("UPDATE employee SET employeeName=?,age=?,location=?, qualifications=? WHERE employeeID=?");
	$updateProfileQuery->bind_param("sissi",$employeeName,$age,$location,$qualifications,$employeeID);
	$result=$updateProfileQuery->execute();

	if($result){
		$status=1;
	}

	$updateProfileQuery->close();
	$connection->close();

	return $status;
}

// function for reading all employees
function readEmployees(){
	$options="";
	$connection=createConnection();
	
	$readEmployeeQuery = $connection->prepare("SELECT * FROM employee");
	$readEmployeeQuery->execute();

	$result = $readEmployeeQuery->get_result();

	while ($row = $result->fetch_assoc()) {
		$option='<option value="'.$row["employeeID"].'">'.$row["employeeName"].'</option>';
		$options.=$option;
	}

	$readEmployeeQuery->close();
	$connection->close();

	return $options;
}

// function for adding a task to the database
function addTask($employeeID,$taskName,$taskDescription,$dueDate){
	$status=0;
	$connection=createConnection();

	$addTaskQuery = $connection->prepare("INSERT INTO task (employeeID,taskName,taskDescription,dueDate) VALUES (?, ?,?,STR_TO_DATE(?, '%Y-%m-%d'))");
	$addTaskQuery->bind_param("isss", $employeeID, $taskName,$taskDescription,$dueDate);
	$result=$addTaskQuery->execute();

	if($result){
		$status=1;
	}

	$addTaskQuery->close();
	$connection->close();

	return $status;
}

// function for getting the information for all tasks  from the database asn an admin
function populateTaskTable(){
	$html="";

	$connection=createConnection();
	
	$populateTaskTableQuery = $connection->prepare("SELECT * FROM task");
	$populateTaskTableQuery->execute();

	$result = $populateTaskTableQuery->get_result();

	while ($row = $result->fetch_assoc()) {
		$status='<td><p class="dash-lable mb-0 bg-danger bg-opacity-10 text-danger rounded-2">Pending</p></td>';

		if($row["status"]==1){
			$status='<td><p class="dash-lable mb-0 bg-success bg-opacity-10 text-success rounded-2">Completed</p></td>';
		}
		$html.='
		<tr>
            <td>
                <div class="d-flex align-items-center gap-3">
                	<p class="mb-0">'.$row["taskName"].'</p>
                </div>
            </td>
            <td><p class="mb-0">'.$row["taskDescription"].'</p></td>
            <td>Julia Sunota</td>
            <td><p class="mb-0">'.$row["dueDate"].'</p></td>';
        $html.=$status;
        $html.='</tr>';
	}

	$populateTaskTableQuery->close();
	$connection->close();
	return $html;				
}

// function to getting all the information on tasks for a particular user
function populateTaskTableUser($employeeID){
	$html="";

	$connection=createConnection();
	
	$populateTaskTableUserQuery = $connection->prepare("SELECT * FROM task WHERE employeeID=?");
	$populateTaskTableUserQuery->bind_param("i", $employeeID);
	$populateTaskTableUserQuery->execute();

	$result = $populateTaskTableUserQuery->get_result();

	while ($row = $result->fetch_assoc()) {

		$status='<td><input type="submit" class="btn btn-success" name="completeTask" value="Mark As Complete"></td>';
		
		if($row["status"]==1){
			$status='<td><p class="dash-lable mb-0 bg-success bg-opacity-10 text-sucess rounded-2">Complete</p></td>';
		}
		
		$html.='
		<tr>
			<form method="POST">
			<input type="text" value="'.$row['taskID'].'" name="taskID" hidden>
            <td>
                <div class="d-flex align-items-center gap-3">
                	<p class="mb-0">'.$row["taskName"].'</p>
                </div>
            </td>
            <td><p class="mb-0">'.$row["taskDescription"].'</p></td>
            <td><p class="mb-0">'.$row["dueDate"].'</p></td>';
            $html.=$status;

        $html.='
            </form>
        </tr>';
	}

	$populateTaskTableUserQuery->close();
	$connection->close();
	return $html;				
}

// function to serch through tasks 
function populateTaskSearchUser($employeeID,$searchTerm){
	$html="";

	$connection=createConnection();
	
	$populateTaskTableUserQuery = $connection->prepare("SELECT * FROM task WHERE employeeID=? AND taskName LIKE ?");
	$searchTerm='%'.$searchTerm.'%';
	$populateTaskTableUserQuery->bind_param("is", $employeeID,$searchTerm);
	$populateTaskTableUserQuery->execute();

	$result = $populateTaskTableUserQuery->get_result();

	while ($row = $result->fetch_assoc()) {

		$status='<td><input type="submit" class="btn btn-success" name="completeTask" value="Mark As Complete"></td>';
		
		if($row["status"]==1){
			$status='<td><p class="dash-lable mb-0 bg-success bg-opacity-10 text-sucess rounded-2">Complete</p></td>';
		}
		
		$html.='
		<tr>
			<form method="POST">
			<input type="text" value="'.$row['taskID'].'" name="taskID" hidden>
            <td>
                <div class="d-flex align-items-center gap-3">
                	<p class="mb-0">'.$row["taskName"].'</p>
                </div>
            </td>
            <td><p class="mb-0">'.$row["taskDescription"].'</p></td>
            <td><p class="mb-0">'.$row["dueDate"].'</p></td>';
            $html.=$status;

        $html.='
            </form>
        </tr>';
	}

	$populateTaskTableUserQuery->close();
	$connection->close();
	return $html;				
}

// function to read review information for an employee
function populateReviewTableUser($employeeID){
	$html="";

	$connection=createConnection();
	
	$populateTaskTableUserQuery = $connection->prepare("SELECT * FROM task WHERE employeeID=?");
	$populateTaskTableUserQuery->bind_param("i", $employeeID);
	$populateTaskTableUserQuery->execute();

	$result = $populateTaskTableUserQuery->get_result();

	$reviewQuery = $connection->prepare("SELECT * FROM review WHERE taskID=?");

	while ($row = $result->fetch_assoc()) {

		$taskID=$row["taskID"];
		$taskName=$row["taskName"];

		$stars='<td><div class="product-rating text-warning">';
		//fetch reviews
		$reviewQuery->bind_param("i", $taskID);
		$reviewQuery->execute();

		$reviews = $reviewQuery->get_result();

		while ($rowReview = $reviews->fetch_assoc()) {
			$rating=$rowReview['rating'];

			for($i=0;$i<$rating;$i++){
				$stars.='<i class="bi bi-star-half"></i>';
			}


			$stars.='</div></td>';
			$html.='
			<tr>
	            <td>
	                <div class="d-flex align-items-center gap-3">
	                	<p class="mb-0">'.$taskName.'</p>
	                </div>
	            </td>';

	        $html.=$stars;

	        $html.='
	            <td><p class="mb-0">'.$rowReview["comments"].'</p></td>
	            <td><p class="mb-0">'.$rowReview["reviewDate"].'</p></td>
	        </tr>';

		}
		
	}
	$reviewQuery->close();
	$populateTaskTableUserQuery->close();
	$connection->close();
	return $html;				
}

// function to update a tasks information
function updateTask($taskID){
	$status=0;

	$connection=createConnection();
	
	$updateTaskQuery = $connection->prepare("UPDATE task SET status=1 WHERE taskID=?");
	$updateTaskQuery->bind_param("i",$taskID);
	$result=$updateTaskQuery->execute();

	if($result){
		$status=1;
	}

	$updateTaskQuery->close();
	$connection->close();

	return $status;
}

// function for reading all the tasks in the database
function readTasks(){
	$options="";
	$connection=createConnection();
	
	$readTaskQuery = $connection->prepare("SELECT * FROM task");
	$readTaskQuery->execute();

	$result = $readTaskQuery->get_result();

	$checkReviewQuery = $connection->prepare("SELECT * FROM review WHERE taskID=?");

	while ($row = $result->fetch_assoc()) {
		$taskID=$row["taskID"];
		$exists=0;
		//check if it is reviewed
		
		$checkReviewQuery->bind_param("i",$taskID);
		$checkReviewQuery->execute();
		

		$checkResult = $checkReviewQuery->get_result();

		while ($rowReview = $checkResult->fetch_assoc()) {
			$exists=1;
		}
		//end check
		if($exists==0){
			$option='<option value="'.$row["taskID"].'">'.$row["taskName"].'</option>';
			$options.=$option;
		}
		
	}

	$checkReviewQuery->close();
	$readTaskQuery->close();
	$connection->close();

	return $options;
}

// function for adding a review to the database
function addReview($taskID,$rating,$comments){
	$status=0;
	$connection=createConnection();

	$date=date('Y-m-d');

	$addReviewQuery = $connection->prepare("INSERT INTO review (taskID,rating,comments,reviewDate) VALUES (?, ?,?,STR_TO_DATE(?, '%Y-%m-%d'))");
	$addReviewQuery->bind_param("iiss", $taskID, $rating,$comments,$date);
	$result=$addReviewQuery->execute();

	if($result){
		$status=1;
	}

	$addReviewQuery->close();
	$connection->close();

	return $status;
}

// function for reading review information from the database
function populateReviewTable(){
	$html="";

	$connection=createConnection();
	
	$populateTaskTableUserQuery = $connection->prepare("SELECT * FROM task LEFT JOIN review on task.taskID=review.taskID");
	$populateTaskTableUserQuery->execute();

	$result = $populateTaskTableUserQuery->get_result();


	while ($row = $result->fetch_assoc()) {

		$taskID=$row["taskID"];
		$taskName=$row["taskName"];

		$stars='<td><div class="product-rating text-warning">';
		

		$rating=$row['rating'];

		for($i=0;$i<$rating;$i++){
			$stars.='<i class="bi bi-star-half"></i>';
		}


		$stars.='</div></td>';
		$html.='
			<tr>
	            <td>
	                <div class="d-flex align-items-center gap-3">
	                	<p class="mb-0">'.$taskName.'</p>
	                </div>
	            </td>';

	    $html.=$stars;

	    $html.='
	            <td><p class="mb-0">'.$row["comments"].'</p></td>
	            <td><p class="mb-0">'.$row["reviewDate"].'</p></td>
	        </tr>';

	}

	$populateTaskTableUserQuery->close();
	$connection->close();
	return $html;				
}


// running the login code when the login button is clicked
if(isset($_POST["login"])){
	$email=$_POST["email"];
	$password=$_POST["password"];

	login($email,$password);

}
// running the register code when the register button is clicked
if(isset($_POST["register"])){
	$email=$_POST["email"];
	$password=$_POST["password"];

	$name=$_POST["name"];
	$age=$_POST["age"];
	$location=$_POST["location"];

	$status=register($email,$password,$name,$age,$location);

	if($status==1){
		$_SESSION['login_suc']="Registration Succesful. Login to Proceed";
		header("location:../login");
	}else{
		$_SESSION["register_err"]="Not Registered";
	}
}

// running the update profile code when the update profile button is clicked
if(isset($_POST["updateProfile"])){
	$employeeID=$_SESSION['employeeID'];

	$name=$_POST["name"];
	$age=$_POST["age"];
	$location=$_POST["location"];
	$qualifications=$_POST["qualifications"];

	$result=updateProfile($employeeID,$name,$age,$location,$qualifications);

	if($result==1){
		$_SESSION['updateProfile_suc']="Profile Updated Successfully";
	}
	
}

// running the add task code when the add task button is clicked
if(isset($_POST['addTask'])){
	$employeeID=$_POST['employeeID'];

	$taskName=$_POST["taskName"];
	$taskDescription=$_POST["taskDescription"];
	$dueDate=$_POST["dueDate"];

	$result=addTask($employeeID,$taskName,$taskDescription,$dueDate);

	if($result==1){
		$_SESSION['task_suc']="Task Added Successfully";
	}else{
		$_SESSION['task_err']="Task Not Added";
	}
}

// running the update task code when the update task button is clicked

if(isset($_POST["completeTask"])){
	$taskID=$_POST["taskID"];
	$result=updateTask($taskID);

	if($result==1){
		$_SESSION['taskUser_suc']="Task Completed";
	}else{
		$_SESSION['taskUser_err']="Task Not Updated";
	}
}

// running the search code when the a employee types in the search bar
if(isset($_POST["searchTerm"]) && isset($_SESSION["employeeID"])){
	$employeeID=$_SESSION["employeeID"];
	$searchTerm=$_POST["searchTerm"];
	echo populateTaskSearchUser($employeeID,$searchTerm);
}

// running the add review code when the add review button is clicked

if(isset($_POST["addReview"])){
	$taskID=$_POST["taskID"];
	$rating=$_POST["rating"];
	$comments=$_POST["comments"];


	$result=addReview($taskID,$rating,$comments);


	if($result==1){
		$_SESSION['review_suc']="Task Reviewed";
	}else{
		$_SESSION['review_err']="Task Not Updated";
	}
}



?>