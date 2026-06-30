<?php
include('./../../assets/php/controller.php');

?>
<html lang="en" data-bs-theme="light">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Reviews- Employee Manager</title>
  <!--favicon-->
	<link rel="icon" href="../../assets/images/favicon-32x32.png" type="image/png">

  <!--plugins-->
  <link href="../../assets/plugins/perfect-scrollbar/css/perfect-scrollbar.css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="../../assets/plugins/metismenu/metisMenu.min.css">
  <link rel="stylesheet" type="text/css" href="../../assets/plugins/metismenu/mm-vertical.css">
  <link rel="stylesheet" type="text/css" href="../../assets/plugins/simplebar/css/simplebar.css">

  <!--bootstrap css-->
  <link href="../../assets/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Material+Icons+Outlined" rel="stylesheet">
  <!--main css-->
  <link href="../../assets/css/bootstrap-extended.css" rel="stylesheet">
  <link href="../../sass/main.css" rel="stylesheet">
  <link href="../../sass/dark-theme.css" rel="stylesheet">
  <link href="../../sass/blue-theme.css" rel="stylesheet">
  <link href="../../sass/semi-dark.css" rel="stylesheet">
  <link href="../../sass/bordered-theme.css" rel="stylesheet">
  <link href="../../sass/responsive.css" rel="stylesheet">

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
             <img src="../../assets/images/avatars/01.png" class="rounded-circle p-1 border" width="45" height="45" alt="">
          </a>
          <div class="dropdown-menu dropdown-user dropdown-menu-end shadow">
            <hr class="dropdown-divider">
            <a class="dropdown-item d-flex align-items-center gap-2 py-2" href="../../logout"><i
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
        <h6 class="mb-0">Employee Manager Admin</h6>
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

           <li  class="active">
            <a href="javascript:;">
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
        <div class="breadcrumb-title pe-3">Admin</div>
        <div class="ps-3">
          <nav aria-label="breadcrumb">
            <ol class="breadcrumb mb-0 p-0">
              <li class="breadcrumb-item"><a href="javascript:;"><i class="bx bx-home-alt"></i></a>
              </li>
              <li class="breadcrumb-item active" aria-current="page">Reviews</li>
            </ol>
          </nav>
        </div>
      
      </div>
      <!--end breadcrumb-->

        <div class="row">

           <div class="col-12 col-xl-12">
            <div class="card rounded-4 border-top border-4 border-primary border-gradient-1">
              <div class="card-body p-4">
                 <p style="color:green;">
                      <?php
                      if(isset($_SESSION['review_suc'])){
                        $_SESSION['review_err']="";
                        echo $_SESSION['review_suc'];
                      }
                      ?>
                    </p>
                     <p style="color:red;">
                      <?php
                      if(isset($_SESSION['review_err'])){
                        $_SESSION['review_suc']="";
                        echo $_SESSION['review_err'];
                      }
                      ?>
                    </p>
                <div class="d-flex align-items-start justify-content-between mb-3">
                  <div class="">
                    <h5 class="mb-0 fw-bold">Add Review</h5>
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
                    <label for="input1" class="form-label">Select Task</label>
                    <select class="form-control" name="taskID">
                      <option value="">Click to Select Task</option>
                      <?php
                        echo readTasks();
                      ?>
                    </select>
                  </div>
                
                  <div class="col-md-12">
                    <label for="input3" class="form-label">Rating</label>
                    <select class="form-control" name="rating">
                      <option value="">Click to Select Rating</option>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                      <option value="6">6</option>
                      <option value="7">7</option>
                      <option value="8">8</option>
                      <option value="9">9</option>
                      <option value="10">10</option>
                    </select>
                  </div>
                
                  <div class="col-md-12">
                    <label for="input11" class="form-label">Review</label>
                    <textarea class="form-control" name="comments" placeholder="Enter Task Review" rows="4" cols="4"></textarea>
                  </div>

                  <div class="col-md-12">
                    <div class="d-md-flex d-grid align-items-center gap-3">
                      <input type="submit" class="btn btn-grd-primary px-4" value="Add Review" name="addReview">
                    </div>
                  </div>
                </form>
              </div>
            </div>
           </div>  
           
           <div class="col-12 col-xl-12">
             <div class="card mt-4">
        <div class="card-body">
          <h5 class="mb-3 fw-bold">Ratings & Reviews<span class="fw-light ms-2"></span></h5>
          <div class="product-table">
            <div class="table-responsive white-space-nowrap">
              <table class="table align-middle">
                <thead class="table-light">
                  <tr>
                    <th>Task Name</th>
                    <th>Rating</th>
                    <th>Review</th>
                    <th>Date Reviewed</th>
                  </tr>
                </thead>
                <tbody>
                </tbody>
                  <?php
                    echo populateReviewTable();
                  ?>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

           
                 
               
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
  <script src="../../assets/js/bootstrap.bundle.min.js"></script>

  <!--plugins-->
  <script src="../../assets/js/jquery.min.js"></script>
  <!--plugins-->
  <script src="../../assets/plugins/perfect-scrollbar/js/perfect-scrollbar.js"></script>
  <script src="../../assets/plugins/metismenu/metisMenu.min.js"></script>
  <script src="../../assets/plugins/simplebar/js/simplebar.min.js"></script>
  <script src="../../assets/js/main.js"></script>
  <script>
    new PerfectScrollbar(".customer-notes")
  </script>


</body>

</html>