<template>
  <div class="feature-toggle-project">
    <div class="project-features">
      <div class="feature-header">
        <div class="project-name">Feature toggles</div>
        <div class="search-box">
          <input type="text" placeholder="Search..." />
        </div>
        <a class="new-feature" @click="openFeature"> New Feature Toggle </a>
      </div>
    </div>

    <table class="feature-table">
      <thead>
        <tr>
          <th>Feature Name</th>
          <th>Dev Enabled</th>
          <th>Prod Enabled</th>
          <th>Date</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(feature, index) in featureToggles" :key="index">
          <td>
            <a href="#" @click.prevent="openEditDialog(feature)">{{
              feature.featureName
            }}</a>
          </td>
          <td>{{ feature.devEnabled ? "Yes" : "No" }}</td>
          <td>{{ feature.prodEnabled ? "Yes" : "No" }}</td>
          <td>{{ feature.dateCreated }}</td>
        </tr>
      </tbody>
    </table>
  </div>

  <v-dialog v-model="dialog" max-width="100%">
    <div class="nn-dialog">
      <v-card>
        <v-text-field label="Enter Feature Name" v-model="featureName" />
        <div class="env-enabled">
          <v-switch
            label="Dev Enabled"
            color="primary"
            v-model="devEnabled"
            inset
          />

          <v-switch
            label="Prod Enabled"
            color="primary"
            v-model="prodEnabled"
            inset
          />
        </div>
        <div class="feature-criteria">
          <v-combobox
            v-model="selectedItem"
            label="Combobox"
            :items="['UserId', 'Factory Group']"
          />
        </div>

        <v-text-field v-if="selectedItem === 'UserId'" label="Enter User ID" />
      </v-card>
      <v-card>Hi </v-card>
    </div>
    <v-card-actions class="margin-top">
      <v-btn color="primary" @click="closeFeature">Close</v-btn>
      <v-btn color="primary" @click="saveFeatureToStore">Save</v-btn>
    </v-card-actions>
  </v-dialog>
</template>


<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      modalActive: false,
      dialog: false,
      enabled: true,
      prodEnabled: true,
      devEnabled: false,
      featureName: "",
      selectedItem: "",
    };
  },
  computed: {
    ...mapState(["featureToggles"]),
  },
  methods: {
    openFeature() {
      this.modalActive = true;
      this.dialog = true;
    },
    closeFeature() {
      this.modalActive = false;
      this.dialog = false;
    },

    saveFeatureToStore() {
      if (this.featureToEdit) {
        // Update existing feature
        this.featureToEdit.featureName = this.featureName;
        this.featureToEdit.devEnabled = this.devEnabled;
        this.featureToEdit.prodEnabled = this.prodEnabled;
      } else {
        // Add new feature
        const newFeature = {
          featureName: this.featureName,
          devEnabled: this.devEnabled,
          prodEnabled: this.prodEnabled,
          dateCreated: new Date().toLocaleString(),
        };
        this.$store.dispatch("saveFeature", newFeature);
      }
      this.closeFeature(); // Optionally close the dialog after saving
    },
    openEditDialog(feature) {
      this.featureName = feature.featureName;
      this.devEnabled = feature.devEnabled;
      this.prodEnabled = feature.prodEnabled;
      this.featureToEdit = feature;
      this.openFeature();
    },
  },
};
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
.nn-dialog {
  border-radius: 10px;
  display: flex !important;
  margin: 2px;
  padding: 10px;
  height: 500px;
  width: 100%;
}
.input-dialog {
  background-color: black;
}
.selected-dialog {
  background-color: red;
}
.project-features {
  background-color: rgb(255, 255, 255);
  border-radius: 12px;
  margin: 26px;
  padding: 10px;
  position: relative;
}
.env-enabled {
  display: flex;
  gap: 10px;
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

.modal {
  background-color: rgba(0, 0, 0, 0.5);
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  justify-content: center;
  align-items: center;
}

.modal.is-active {
  display: flex;
}

.modal-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
}

.modal-close {
  position: absolute;
  top: 10px;
  right: 10px;
}
.margin-top {
  margin-top: 30px;
}
</style>