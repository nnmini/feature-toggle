<template>
  <div class="feature-toggle-project">
    <div class="project-card">
      <div class="project-name">My Project</div>
    </div>

    <div class="project-features">
      <div class="feature-header">
        <div class="project-name">Feature toggles</div>
        <div class="search-box">
          <input type="text" placeholder="Search..." />
        </div>
        <a href="#" class="new-feature">New Feature Toggle</a>
      </div>
    </div>

    <table class="feature-table">
      <thead>
        <tr>
          <th>Feature Name</th>
          <th>Enabled</th>
          <th>Date Created</th>
        </tr>
      </thead>
      <tbody>
        <!-- Rows for feature toggles will go here -->
        <!-- Example row:
          <tr>
            <td>Feature 1</td>
            <td>Yes</td>
            <td>2024-05-06</td>
          </tr>
          -->
      </tbody>
    </table>
  </div>
</template>


<script>
export default {};
</script>



<style scoped>
@import "./css/style.css";

.project-card {
  background-color: rgb(255, 255, 255);
  border-radius: 12px;
  margin: 26px;
  padding: 10px;
  position: relative;
}
.project-features {
  background-color: rgb(255, 255, 255);
  border-radius: 12px;
  margin: 26px;
  padding: 10px;
  position: relative;
}
.project-name {
  font-size: 16px;
  margin: 10px;
  background-color: white;
}
.break {
  width: 100%;
  background-color: rgb(225, 225, 227);
  height: 1px;
}

.search-box {
  margin-top: 10px; /* Adjust margin as needed */
}

.search-box input[type="text"] {
  width: 100%;
  padding: 8px;
  border-radius: 8px;

  border: 1px solid #ccc;
  box-sizing: border-box;
  font-size: 14px;
}
#button {
  display: block;
}
.feature-header {
  display: flex;
  justify-content: space-between; /* Distribute space between children */
  align-items: center; /* Vertically align items */
}

.new-feature {
  display: inline-block;
  padding: 8px 16px; /* Adjust padding as needed */
  border: none;
  border-radius: 8px;
  background-color: #007bff; /* Change color to your preference */
  color: #fff; /* Text color */
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease; /* Smooth transition */
}

.new-feature:hover {
  background-color: #0056b3; /* Darker shade on hover */
}
.feature-table {
  width: 95%;

  margin-top: 10px; /* Adjust margin as needed */
  background-color: rgb(255, 255, 255);
  border-radius: 12px;
  margin: 26px;
  margin-top: 1px;
  padding: 10px;
  position: relative;
}

.feature-table th,
.feature-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.feature-table th {
  background-color: #f2f2f2;
}
</style>