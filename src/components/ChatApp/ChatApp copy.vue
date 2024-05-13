<template>
  <div class="app-container">
    <nav class="navbar navbar-dark bg-dark" ref="navbar">
      <span class="navbar-brand mb-0 h1 app-name">Chat App</span>
    </nav>

    <div class="content">
      <div v-show="isSidebarOpen" class="sidebar-pane" ref="sidebar">
        <div class="chat-messages">
          <!-- Display chat messages -->
          <div v-for="(message, index) in messages" :key="index">
            {{ message }}
          </div>
        </div>
        <div class="input-container">
          <input
            v-model="inputMessage"
            type="text"
            placeholder="Enter your question"
            class="chat-input-text"
            @keyup.enter="sendMessage"
          />
        </div>
      </div>

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
    </div>

    <div class="chat-icon" @click="toggleSidebar">
      <!-- Replace with your actual chat icon -->
      <i class="fas fa-comments"></i>
    </div>
  </div>
</template>
  
  <script>
import "@fortawesome/fontawesome-free/css/all.css";
import { AgGridVue } from "ag-grid-vue3";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";
import axios from "axios";

export default {
  components: {
    AgGridVue,
  },
  data() {
    return {
      isSidebarOpen: false,
      tableKey: 0,
      inputMessage: "",
      messages: [],
      columnDefs: [
        { headerName: "Make", field: "make" },
        { headerName: "Model", field: "model" },
        { headerName: "Price", field: "price" },
      ],
      defaultColDef: {
        sortable: true,
        filter: true,
      },
      rowData: [
        { make: "Toyota", model: "Celica", price: 35000 },
        { make: "Ford", model: "Mondeo", price: 32000 },
        { make: "Porsche", model: "Boxster", price: 72000 },
      ],
      tableHeight: "500px",
      sidebarWidth: "350px",
      gridApi: null,
    };
  },
  methods: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
      this.adjustTableHeight();
    },

    sendMessage() {
      this.messages.push(this.inputMessage);
      axios
        .post("http://localhost:5000/process_user_input", {
          user_input: this.inputMessage,
        })
        .then((response) => {
          console.log("response...", response);
          this.handleResponse(response.data);
        })
        .catch((error) => {
          console.error("Error processing user input:", error);
        });

      this.inputMessage = "";
    },

    handleResponse(response) {
      if (response.response.action === "select") {
        console.log("select....");
        this.selectRow(response.response.rowNumber);
      } else if (response.response.action === "edit") {
        console.log("edit....");
        // Call a method to perform the edit action
        this.editRow(response.response.rowNumber);
      }
      this.messages.push(response.response);
    },

    selectRow(rowNumber) {
      console.log("rowNumber....", rowNumber);
      if (this.gridApi) {
        this.gridApi.forEachNode((node) => {
          if (node.rowIndex === rowNumber - 1) {
            node.setSelected(true);
          }
        });
      }
    },
    editRow(rowNumber) {
      // Perform edit action
      // For demonstration purposes, let's update the row data
      console.log("editRow....", rowNumber);
      this.selectRow(rowNumber);
      const newData = {
        make: "EditedMake",
        model: "EditedModel",
        price: 99999,
      };

      // Create a new array with updated row data
      const updatedRowData = this.rowData.map((row, index) => {
        if (index === rowNumber - 1) {
          return newData;
        }
        return row;
      });

      // Assign the new array to rowData
      this.rowData = updatedRowData;

      this.tableKey++;
    },

    adjustTableHeight() {
      if (this.isSidebarOpen) {
        const navbarHeight = this.$refs.navbar.clientHeight;
        const sidebarHeight = this.$refs.sidebar.clientHeight;
        this.tableHeight = `calc(100vh - ${navbarHeight}px - ${sidebarHeight}px - 20px)`;
      } else {
        this.tableHeight = "calc(100vh - 60px)"; // Height of navbar
      }
    },

    onGridReady(params) {
      this.gridApi = params.api;
    },
  },
  mounted() {
    window.addEventListener("resize", this.adjustTableHeight);
  },
  unmounted() {
    window.removeEventListener("resize", this.adjustTableHeight);
  },
};
</script>
  
 
  
  <style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  color: #333;
  line-height: 1.6;
}

.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.navbar {
  background-color: #343a40 !important;
  color: #fff;
  padding: 10px;
}

.navbar-brand {
  font-size: 1.5rem;
}

.content {
  display: flex;
}

.sidebar-pane {
  background-color: #f4f4f4;
  width: 350px;
  display: flex;
  flex-direction: column;
}

.chat-messages {
  padding: 10px;
  flex: 1;
  overflow-y: auto;
}

.input-container {
  position: relative;
}

.chat-input-text {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.data {
  flex-grow: 1;
  position: relative;
}

.ag-theme-alpine {
  height: 100%;
}

.chat-icon {
  position: fixed;
  bottom: 40px;
  right: 20px;
  cursor: pointer;
  z-index: 1000;
}

.chat-icon .fas {
  font-size: 30px;
}
</style>
  