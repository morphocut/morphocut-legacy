<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Projects</h1>
        <hr>
        <br>
        <br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.dataset-modal>Add Project</button>
        <br>
        <br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Name</th>
              <th scope="col">Objects</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(dataset, index) in datasets" :key="index">
              <td>{{ dataset.id }}</td>
              <td>{{ dataset.name }}</td>
              <td>{{ dataset.objects }}</td>
              <td>
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  style="margin-left: 0.5rem;"
                  v-on:click="processDataset(dataset)"
                >Process</button>
                <button
                  type="button"
                  class="btn btn-warning btn-sm"
                  style="margin-left: 0.5rem;"
                  v-if="dataset.download_complete"
                  v-on:click="downloadDataset(dataset)"
                >Download</button>
                <div v-if="dataset.download_running">
                  <div class="loader"></div>
                </div>
                <!-- <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  style="margin-left: 0.5rem;"
                  v-on:click="removeDataset(dataset.id)"
                >Delete</button>-->
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <!-- <div v-if="!download_complete">
      <h1>Processing...</h1>
      <div class="loader"></div>
    </div>-->
    <b-modal ref="addDatasetModal" id="dataset-modal" title="Add a new dataset" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group" label="Name:" label-for="form-name-input">
          <b-form-input
            id="form-name-input"
            type="text"
            v-model="addDatasetForm.name"
            required
            placeholder="Enter name"
          ></b-form-input>
        </b-form-group>
        <!-- <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>-->
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      datasets: [],
      //   download_complete: true,
      //   download_path: "",
      addDatasetForm: {
        id: 0,
        name: "",
        objects: 0
      }
    };
  },
  // props: {
  //   dataset
  // },
  methods: {
    getDatasets() {
      const path = "http://localhost:5000/datasets";
      axios
        .get(path)
        .then(res => {
          this.datasets = res.data.datasets;
          console.log(this.datasets);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addDataset(payload) {
      const path = "http://localhost:5000/datasets";
      axios
        .post(path, payload)
        .then(() => {
          this.getDatasets();
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
          this.getDatasets();
        });
    },
    processDataset(dataset) {
      const path = "http://localhost:5000/datasets/" + dataset.id + "/process";
      this.$set(dataset, "download_complete", false);
      //   dataset.download_complete = false;
      dataset.download_running = true;
      console.log(
        "download_running: " +
          dataset.download_running +
          ", " +
          dataset.download_complete
      );
      axios.get(path).then(res => {
        dataset.download_path = res.data.download_path;
        this.$set(dataset, "download_complete", true);
        dataset.download_running = false;
        axios.get("http://localhost:5000/" + dataset.download_path);
      });
    },
    downloadDataset(dataset) {
      const path = "http://localhost:5000/" + dataset.download_path;
      axios({
        url: path,
        method: "GET",
        responseType: "blob" // important
      }).then(response => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", dataset.download_path);
        document.body.appendChild(link);
        link.click();
      });
    },
    initForm() {
      this.addDatasetForm.id = 0;
      this.addDatasetForm.name = "";
      this.addDatasetForm.objects = 0;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addDatasetModal.hide();
      const payload = {
        id: this.addDatasetForm.id,
        name: this.addDatasetForm.name,
        objects: this.addDatasetForm.objects
      };
      this.addDataset(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addDatasetModal.hide();
      this.initForm();
    }
  },
  created() {
    this.getDatasets();
  }
};
</script>

<style>
.loader {
  border: 5px solid #f3f3f3; /* Light grey */
  border-top: 5px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>