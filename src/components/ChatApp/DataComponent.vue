<template>
  <div class="data">
    <div class="ag-theme-alpine" :style="{ height: tableHeight }">
      <ag-grid-vue
        style="width: 100%; height: 100%"
        class="ag-theme-alpine"
        :rowData="rowData"
        :columnDefs="columnDefs"
        :defaultColDef="defaultColDef"
        :domLayout="'autoHeight'"
        @grid-ready="onGridReady"
      ></ag-grid-vue>
    </div>
  </div>
</template>
  
  <script>
import { AgGridVue } from "ag-grid-vue3";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";

export default {
  components: {
    AgGridVue,
  },
  props: {
    rowData: Array,
    columnDefs: Array,
    defaultColDef: Object,
    tableHeight: String,
    onGridReady: Function,
  },
};
</script>
  
  <style scoped>
.data {
  flex-grow: 1;
  position: relative;
}
.ag-theme-alpine {
  height: 100%;
}
</style>
  