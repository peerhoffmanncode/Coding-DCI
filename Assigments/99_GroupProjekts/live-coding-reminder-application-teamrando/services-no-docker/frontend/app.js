const { createApp } = Vue;
createApp({
  data() {
    return {
      reminders: [],
      errorMessage: "",
    };
  },
  mounted: async function () {
    try {
      const response = await fetch("http://localhost:5050/reminders");
      this.reminders = await response.json();
      console.debug("loaded...", this.reminders);
    } catch (err) {
      console.error("Failed to load from API");
      this.errorMessage =
        "CANNOT CONNECT TO THE API! Make sure your servers are up";
    }
  },
  methods: {
    async testApi(event) {
      console.log("hello");
    },
    async remove(id) {
      try {
        await fetch(`http://localhost:5050/reminders/${id}`, {
          method: "DELETE",
        });
        this.reminders = this.reminders.filter((r) => r.id != id);
        console.debug(`Deleted reminder ${id}`);
      } catch (err) {
        console.error("Failed with", err);
      }
    },
  },
}).mount("#app");
