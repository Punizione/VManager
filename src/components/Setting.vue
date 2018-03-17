 <template>
 <v-app id="inspire">
    <v-layout column>
      <v-flex xs12 sm6>
        <v-toolbar color="indigo" dark>
          
          <v-toolbar-title>Step</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon>sort</v-icon>
          </v-btn>
          <v-tabs
        color="indigo"
        slot="extension"
        v-model="tab"
                  drak
        grow
                  icons-and-text
      ><v-tabs-slider color="yellow"></v-tabs-slider>
            <v-tab v-for="item in items" :key="item">
          {{ item.text }}
              <v-icon>{{ item.icon }}</v-icon>
        </v-tab>
          </v-tabs>
        </v-toolbar>
        <v-tabs-items v-model="tab">
      <v-tab-item v-for="item in items" :key="item">
        <v-card>
    <v-stepper v-model="steptor" vertical non-linear>
      <v-stepper-step step="1" :complete="steptor > 1" editable edit-icon="done"
                      >
        Select an app
        <small>Summarize if needed</small>
      </v-stepper-step>
      <v-stepper-content step="1">
        <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
        <v-btn color="primary" @click.native="steptor = 2">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step step="2" :complete="steptor > 2" editable edit-icon="done">Configure analytics for this app</v-stepper-step>
      <v-stepper-content step="2">
        <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
        <v-btn color="primary" @click.native="steptor = 3">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step step="3" :complete="steptor > 3" editable edit-icon="done">Select an ad format and name ad unit</v-stepper-step>
      <v-stepper-content step="3">
        <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
        <v-btn color="primary" @click.native="steptor = 4">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>
      <v-stepper-step step="4" editable edit-icon="done">View setup instructions</v-stepper-step>
      <v-stepper-content step="4">
        <v-card color="grey lighten-1" class="mb-5" height="200px"></v-card>
        <v-btn color="primary" @click.native="steptor = 1">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>
    </v-stepper>
          </v-card>
        </v-tab-item>
    </v-tabs-items>
        </v-flex>
    </v-layout>
  </v-app>
  </template>
<script>
export default {
  
}
</script>
