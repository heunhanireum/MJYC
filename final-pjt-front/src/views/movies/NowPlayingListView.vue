<template>
  <div>
    <div>nowplaying</div>
    <div class="container">
      <div class="row">
        <div class="col-3 my-3" v-for="nowplay in nowplaying" :key="nowplay.id">
          <div class="card" style="width: 18rem;">
            <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${nowplay.poster_path}`" class="card-img-top" alt="...">
            <div class="card-body">
              <div class="card-title">{{ nowplay.title }}</div>
              {{ nowplay.movieNum }}
              <router-link :to="{ name: 'moviedetail', params: { movieNum: nowplay.movie_num } }">DETAIL</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'NowPlayingListView',
  computed: {
    ...mapGetters(['nowplaying', 'isnowplaying'])
  },
  methods: {
    ...mapActions(['fetchNowplaying'])
  },
  created() {
    this.fetchNowplaying()
  },
}
</script>

<style>

</style>