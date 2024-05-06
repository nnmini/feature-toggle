
<template>
  <div class="container">
    <div class="el el--1">HTML</div>
    <div class="el el--2">and</div>
    <div class="el el--3">CSS</div>
    <div class="el el--4">are</div>
    <div class="el el--5">amazing</div>
    <div class="el el--6">languages</div>
    <div class="el el--7">to</div>
    <div class="el el--8">learn</div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.el--1 {
  background-color: blueviolet;
}
.el--2 {
  background-color: orangered;
}
.el--3 {
  background-color: green;
  height: 150px;
}
.el--4 {
  background-color: goldenrod;
}
.el--5 {
  background-color: palevioletred;
}
.el--6 {
  background-color: steelblue;
}
.el--7 {
  background-color: yellow;
}
.el--8 {
  background-color: crimson;
}

.container {
  /* STARTER */
  font-family: sans-serif;
  background-color: #ddd;
  font-size: 30px;
  margin: 40px;

  /* FLEXBOX */
  display: flex;

  align-items: center;
  justify-content: flex-start;
  gap: 30px;
}
.el--1 {
  align-self: flex-start;
}

.el--4 {
  align-self: stretch;
}

.el--6 {
  order: -1;
}
</style>