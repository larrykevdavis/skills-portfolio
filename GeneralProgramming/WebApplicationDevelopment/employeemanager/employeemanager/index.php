<?php
include('./assets/php/controller.php')
?>
<html lang="en" data-bs-theme="light">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Home - Employee Manager</title>
  <!--favicon-->
  <link rel="icon" href="assets/images/favicon-32x32.png" type="image/png">
  <!--plugins-->
  <link href="assets/plugins/perfect-scrollbar/css/perfect-scrollbar.css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="assets/plugins/metismenu/metisMenu.min.css">
  <link rel="stylesheet" type="text/css" href="assets/plugins/metismenu/mm-vertical.css">
  <link rel="stylesheet" type="text/css" href="assets/plugins/simplebar/css/simplebar.css">
  <!--bootstrap css-->
  <link href="assets/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Material+Icons+Outlined" rel="stylesheet">
  <!--main css-->
  <link href="assets/css/bootstrap-extended.css" rel="stylesheet">
  <link href="sass/main.css" rel="stylesheet">
  <link href="sass/dark-theme.css" rel="stylesheet">
  <link href="sass/blue-theme.css" rel="stylesheet">
  <link href="sass/semi-dark.css" rel="stylesheet">
  <link href="sass/bordered-theme.css" rel="stylesheet">
  <link href="sass/responsive.css" rel="stylesheet">

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
             <img src="assets/images/avatars/01.png" class="rounded-circle p-1 border" width="45" height="45" alt="">
          </a>
          <div class="dropdown-menu dropdown-user dropdown-menu-end shadow">
            <hr class="dropdown-divider">
            <a class="dropdown-item d-flex align-items-center gap-2 py-2" href="./logout"><i
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
            <a href="javascript:;">
              <div class="parent-icon"><i class="material-icons-outlined">home</i>
              </div>
              <div class="menu-title">Dashboard</div>
            </a>
          </li>
        
          <li>
            <a href="./profile">
              <div class="parent-icon"><i class="material-icons-outlined">person</i>
              </div>
              <div class="menu-title">User Profile</div>
            </a>
          </li>


          <li>
            <a href="./reviews">
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
								<li class="breadcrumb-item active" aria-current="page">Task List</li>
							</ol>
						</nav>
					</div>
					
				</div>
				<!--end breadcrumb-->
     
        <div class="row">
          <div class="col-xxl-8 d-flex align-items-stretch">
            <div class="card w-100 overflow-hidden rounded-4">
              <div class="card-body position-relative p-4">
                <div class="row">
                  <div class="col-12 col-sm-7">
                    <div class="d-flex align-items-center gap-3 mb-5">
                      <img src="assets/images/avatars/01.png" class="rounded-circle bg-grd-info p-1"  width="60" height="60" alt="user">
                      <div class="">
                        <p class="mb-0 fw-semibold">Welcome back</p>
                        <h4 class="fw-semibold mb-0 fs-4 mb-0">
                          <?php
                          if(isset($_SESSION["email"])){
                            echo $_SESSION["email"];
                          }
                          ?>
                        </h4>
                      </div>
                    </div>
                    <div class="d-flex align-items-center gap-5">
                      <div class="">
                        <h4 class="mb-1 fw-semibold d-flex align-content-center">
                          <?php echo date('D - d - M - Y')?>
                          <i class="ti ti-arrow-up-right fs-5 lh-base text-success"></i>
                        </h4>
                        <p class="mb-3"> <?php echo date('h:i:A')?></p>
                        <div class="progress mb-0" style="height:5px;">
                          <div class="progress-bar bg-grd-success" role="progressbar" style="width: 60%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                      </div>
                     
                      <div class="vr"></div>

                     
                    </div>
                  </div>
                  <div class="col-12 col-sm-5">
                    <div class="welcome-back-img pt-4">
                       <img src="assets/images/gallery/welcome-back-3.png" height="180" alt="">
                    </div>
                  </div>
                </div><!--end row-->
              </div>
            </div>
          </div>
         
          <div class="col-lg-12 col-xxl-8 d-flex align-items-stretch">
            <div class="card w-100 rounded-4">
              <div class="card-body">
               <div class="d-flex align-items-start justify-content-between mb-3">
                  <div class="">
                    <h5 class="mb-0">Your Tasks</h5>
                  </div>
                  <div class="dropdown">
                    <a href="javascript:;" class="dropdown-toggle-nocaret options dropdown-toggle"
                      data-bs-toggle="dropdown">
                      <span class="material-icons-outlined fs-5">more_vert</span>
                    </a>
                   
                  </div>
                </div>
                <div class="order-search position-relative my-3">
                  <input class="form-control rounded-5 px-5" type="text" placeholder="Search" onkeyup="search(this)">
                  <span class="material-icons-outlined position-absolute ms-3 translate-middle-y start-0 top-50">search</span>
                </div>
                 <p style="color:green;">
                      <?php
                      if(isset($_SESSION['taskUser_suc'])){
                        $_SESSION['taskUser_err']="";
                        echo $_SESSION['taskUser_suc'];
                      }
                      ?>
                    </p>
                     <p style="color:red;">
                      <?php
                      if(isset($_SESSION['taskUser_err'])){
                        $_SESSION['taskUser_suc']="";
                        echo $_SESSION['taskUser_err'];
                      }
                      ?>

                 <div class="table-responsive">
                     <table class="table align-middle">
                       <thead>
                        <tr>
                          <th>Task Name</th>
                          <th>Task Description</th>
                          <th>Due Date</th>
                          <th>Status</th>
                        </tr>
                       </thead>
                        <tbody id="search">
                          <?php
                          $employeeID=$_SESSION["employeeID"];
                          echo populateTaskTableUser($employeeID);
                          ?>
                          
                        </tbody>
                     </table>
                 </div>
              </div>
            </div>
          </div>
        </div>



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
  <!--end footer-->




  <!--bootstrap js-->
  <script src="assets/js/bootstrap.bundle.min.js"></script>

  <!--plugins-->
  <script src="assets/js/jquery.min.js"></script>
  <!--plugins-->
  <script src="assets/plugins/perfect-scrollbar/js/perfect-scrollbar.js"></script>
  <script src="assets/plugins/metismenu/metisMenu.min.js"></script>
  <script src="assets/plugins/apexchart/apexcharts.min.js"></script>
  <script src="assets/plugins/simplebar/js/simplebar.min.js"></script>
  <script src="assets/plugins/peity/jquery.peity.min.js"></script>
  <script>
    $(".data-attributes span").peity("donut")
  </script>
  <script src="assets/js/main.js"></script>
  <script src="assets/js/dashboard1.js"></script>
  <script>
	   new PerfectScrollbar(".user-list")
  </script>

  <script type="text/javascript">
    function search(elem){
      var searchTerm = $(elem).val();

      $.ajax({
        url: "./assets/php/controller.php",
        type: "POST",
        data:{
          searchTerm: searchTerm
        },
        success: function (response) {
          $('#search').html(response);
        },
        error: function(jqXHR, textStatus, errorThrown) {
           console.log(textStatus, errorThrown);
        }
    });
    }
    
  </script>

</body>

</html>