<?php
include('./../assets/php/controller.php');
$employeeID=$_SESSION["employeeID"];
readProfile($employeeID)
?>
<html lang="en" data-bs-theme="light">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>User Profile - Employee Manager</title>
  <!--favicon-->
  <link rel="icon" href="../assets/images/favicon-32x32.png" type="image/png">

  <!--plugins-->
  <link href="../assets/plugins/perfect-scrollbar/css/perfect-scrollbar.css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="../assets/plugins/metismenu/metisMenu.min.css">
  <link rel="stylesheet" type="text/css" href="../assets/plugins/metismenu/mm-vertical.css">
  <link rel="stylesheet" type="text/css" href="../assets/plugins/simplebar/css/simplebar.css">
  <!--bootstrap css-->
  <link href="../assets/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Material+Icons+Outlined" rel="stylesheet">
  <!--main css-->
  <link href="../assets/css/bootstrap-extended.css" rel="stylesheet">
  <link href="../sass/main.css" rel="stylesheet">
  <link href="../sass/dark-theme.css" rel="stylesheet">
  <link href="../sass/blue-theme.css" rel="stylesheet">
  <link href="../sass/semi-dark.css" rel="stylesheet">
  <link href="../sass/bordered-theme.css" rel="stylesheet">
  <link href="../sass/responsive.css" rel="stylesheet">

</head>

<body>

  <!--start header-->
   <header class="top-header">
    <nav class="navbar navbar-expand align-items-center gap-4">
      <div class="btn-toggle">
        <a href="javascript:;"><i class="material-icons-outlined">menu</i></a>
      </div>
      <div class="search-bar flex-grow-1">
      
      </div>
      <ul class="navbar-nav gap-1 nav-right-links align-items-center">

        <li class="nav-item dropdown">
          <a href="javascrpt:;" class="dropdown-toggle dropdown-toggle-nocaret" data-bs-toggle="dropdown">
             <img src="../assets/images/avatars/01.png" class="rounded-circle p-1 border" width="45" height="45" alt="">
          </a>
          <div class="dropdown-menu dropdown-user dropdown-menu-end shadow">
            <hr class="dropdown-divider">
            <a class="dropdown-item d-flex align-items-center gap-2 py-2" href="javascript:;"><i
            class="material-icons-outlined">power_settings_new</i>Logout</a>
          </div>
        </li>
      </ul>

    </nav>
  </header>
  <!--end top header-->


  <!--start sidebar-->
  <aside class="sidebar-wrapper" data-simplebar="true">
    <div class="sidebar-header">
      <div class="logo-name flex-grow-1">
        <h6 class="mb-0">Employee Manager</h6>
      </div>
      <div class="sidebar-close">
        <span class="material-icons-outlined">close</span>
      </div>
    </div>
    <div class="sidebar-nav">
        <!--navigation-->
        <ul class="metismenu" id="sidenav">
          <li  class="active">
            <a href="../">
              <div class="parent-icon"><i class="material-icons-outlined">home</i>
              </div>
              <div class="menu-title">Dashboard</div>
            </a>
          </li>
        
          <li>
            <a href="javascript:;">
              <div class="parent-icon"><i class="material-icons-outlined">person</i>
              </div>
              <div class="menu-title">User Profile</div>
            </a>
          </li>


          <li>
            <a href="../reviews">
              <div class="parent-icon"><i class="material-icons-outlined">list</i>
              </div>
              <div class="menu-title">Reviews</div>
            </a>
          </li>
         
        
         </ul>
        <!--end navigation-->
    </div>
  </aside>
<!--end sidebar-->


  <!--start main wrapper-->
  <main class="main-wrapper">
    <div class="main-content">
      <!--breadcrumb-->
				<div class="page-breadcrumb d-none d-sm-flex align-items-center mb-3">
					<div class="breadcrumb-title pe-3">Dashboard</div>
					<div class="ps-3">
						<nav aria-label="breadcrumb">
							<ol class="breadcrumb mb-0 p-0">
								<li class="breadcrumb-item"><a href="javascript:;"><i class="bx bx-home-alt"></i></a>
								</li>
								<li class="breadcrumb-item active" aria-current="page">User Profile</li>
							</ol>
						</nav>
					</div>
				</div>
				<!--end breadcrumb-->
      

        <div class="card rounded-4">
          <div class="card-body p-4">
            
              <div class="profile-info pt-5 d-flex align-items-center justify-content-between">
                <div class="">
                  <h3>
                    <?php
                      if(isset($_SESSION["employeeName"])){
                          echo $_SESSION["employeeName"];
                      }
                    ?>
                  </h3>
                  <p class="mb-0">Engineer at Stark Industries<br>
                   New York, United States</p>
                </div>
              </div>
          </div>
        </div>

        <div class="row">
           
           <div class="col-12 col-xl-4">
            <div class="card rounded-4">
              <div class="card-body">
                <div class="d-flex align-items-start justify-content-between mb-3">
                  <div class="">
                    <h5 class="mb-0 fw-bold">Profile Information</h5>
                  </div>
                  <div class="dropdown">
                    <a href="javascript:;" class="dropdown-toggle-nocaret options dropdown-toggle"
                      data-bs-toggle="dropdown">
                      <span class="material-icons-outlined fs-5">more_vert</span>
                    </a>
                   
                  </div>
                 </div>
                 <div class="full-info">
                  <div class="info-list d-flex flex-column gap-3">
                    <div class="info-list-item d-flex align-items-center gap-3"><span class="material-icons-outlined">account_circle</span><p class="mb-0">Full Name: 
                      <?php
                      if(isset($_SESSION["employeeName"])){
                          echo $_SESSION["employeeName"];
                      }
                    ?>
                    </p></div>
                    <div class="info-list-item d-flex align-items-center gap-3"><span class="material-icons-outlined">done</span><p class="mb-0">Age:
                      <?php
                      if(isset($_SESSION["age"])){
                          echo $_SESSION["age"];
                      }
                    ?>
                    </p></div>
                     <div class="info-list-item d-flex align-items-center gap-3"><span class="material-icons-outlined">flag</span><p class="mb-0">Location:
                       <?php
                      if(isset($_SESSION["location"])){
                          echo $_SESSION["location"];
                      }
                    ?>
                     </p></div>
                    <div class="info-list-item d-flex align-items-center gap-3"><span class="material-icons-outlined">code</span><p class="mb-0">Job Title:
                    <?php
                      if(isset($_SESSION["jobTitle"])){
                          echo $_SESSION["jobTitle"];
                      }
                    ?>
                    </p></div>
                   
                    <div class="info-list-item d-flex align-items-center gap-3"><span class="material-icons-outlined">send</span><p class="mb-0">Qualifications: 
                    <?php
                      if(isset($_SESSION["qualifications"])){
                          echo $_SESSION["qualifications"];
                      }
                    ?>
                    </p></div>
                   
                  </div>
                </div>
              </div>
            </div>

           </div>

           <div class="col-12 col-xl-8">
            <div class="card rounded-4 border-top border-4 border-primary border-gradient-1">
              <div class="card-body p-4">
                 <p style="color:green;">
                      <?php
                      if(isset($_SESSION['updateProfile_suc'])){
                        echo $_SESSION['updateProfile_suc'];
                      }
                      ?>
                    </p>
                <div class="d-flex align-items-start justify-content-between mb-3">
                  <div class="">
                    <h5 class="mb-0 fw-bold">Edit Profile</h5>
                  </div>
                  <div class="dropdown">
                    <a href="javascript:;" class="dropdown-toggle-nocaret options dropdown-toggle"
                      data-bs-toggle="dropdown">
                      <span class="material-icons-outlined fs-5">more_vert</span>
                    </a>
                  </div>
                 </div>
                <form class="row g-4" method="POST">
                  <div class="col-md-12">
                    <label for="input1" class="form-label">Full Name</label>
                    <input type="text" class="form-control" name="name" value="<?php if(isset($_SESSION["employeeName"])){echo $_SESSION["employeeName"];}?>">
                  </div>
                
                  <div class="col-md-12">
                    <label for="input3" class="form-label">Age</label>
                    <input type="text" class="form-control" name="age" placeholder="age" value="<?php if(isset($_SESSION["age"])){echo $_SESSION["age"];}?>">
                  </div>
                  <div class="col-md-12">
                    <label for="input4" class="form-label">Location</label>
                    <input type="text" class="form-control" name="location" value="<?php if(isset($_SESSION["location"])){echo $_SESSION["location"];}?>">
                  </div>
                  
                  <div class="col-md-12">
                    <label for="input11" class="form-label">Qualifications</label>
                    <textarea class="form-control" name="qualifications" placeholder="Enter Qualifications" rows="4" cols="4"><?php if(isset($_SESSION["qualifications"])){echo $_SESSION["qualifications"];}?></textarea>
                  </div>
                  <div class="col-md-12">
                    <div class="d-md-flex d-grid align-items-center gap-3">
                      <input type="submit" class="btn btn-grd-primary px-4" value="Update Profile" name="updateProfile">
                    </div>
                  </div>
                </form>
              </div>
            </div>
           </div>  
        </div><!--end row-->
       


    </div>
  </main>
  <!--end main wrapper-->


    <!--start overlay-->
    <div class="overlay btn-toggle"></div>
    <!--end overlay-->


     <!--start footer-->
     <footer class="page-footer">
      <p class="mb-0">Copyright © 2025. All right reserved.</p>
    </footer>
    <!--top footer-->



  <!--bootstrap js-->
  <script src="../assets/js/bootstrap.bundle.min.js"></script>

  <!--plugins-->
  <script src="../assets/js/jquery.min.js"></script>
  <!--plugins-->
  <script src="../assets/plugins/perfect-scrollbar/js/perfect-scrollbar.js"></script>
  <script src="../assets/plugins/metismenu/metisMenu.min.js"></script>
  <script src="../assets/plugins/simplebar/js/simplebar.min.js"></script>
  <script src="../assets/js/main.js"></script>


</body>

</html>