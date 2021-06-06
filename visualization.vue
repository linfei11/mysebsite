<template>
  <el-card>
    <div id="main" style="width: 600px; height: 600px"></div>
  </el-card>
</template>

<script>
import * as echarts from "echarts";
export default {
  name: "visual",
  data() {
    return {
      charts: "",
      attackType: [
        "普通木马",
        "QM木马",
        "漏洞利用",
        "恶意IP",
        "恶意域名",
        "恶意URL",
        "恶意邮箱",
      ],
      attackData: [],
      statisticsDict: {
        Trojan: 0,
        QM_Trojan: 0,
        Exploit: 0,
        Black_IP: 0,
        Black_Domain: 0,
        Black_URL: 0,
        Black_Mail: 0,
      },
      ruleData: [],
      opinionData: [
        { value: 335, name: "直接访问" },
        { value: 0, name: "邮件营销" },
        { value: 234, name: "联盟广告" },
        { value: 1548, name: "搜索引擎" },
      ],
    };
  },
  mounted() {
    // this.getAttackList();
    this.getAttackList()
  },
  methods: {
    drawPie() {
      //基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById("main"));

      // 绘制图表
      myChart.setOption({
        title: {
          text: "攻击类型占比图",
          left: "center",
        },
        tooltip: {
          trigger: "item",
        },
        legend: {
          orient: "vertical",
          left: "left",
        },
        series: [
          {
            name: "攻击数量",
            type: "pie",
            radius: ["50%", "70%"],
            data: this.ruleData,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      });
    },
    getAttackList () {
      this.axios({
        url: "attacks/?format=json",
        method: "get",
        async: false
      }).then((res) => {
        if (res.status !== 200) return this.$message.error("error");
        this.attackData = res.data;
        this.statistics();
      });
    },
    statistics() {
      for (var i = 0; i < this.attackData.length; i++) {
        for (var key in this.statisticsDict) {
          if (this.attackData[i].rule_type == key) {
            this.statisticsDict[key]++;
          }
        }
      }
      //console.log(this.statisticsDict);
      var temsig = 0;
      for (var key in this.statisticsDict) {
        this.ruleData.push({
          value: this.statisticsDict[key],
          name: this.attackType[temsig],
        });
        temsig++;
      }
      this.drawPie("main")
      //console.log(this.ruleData);
      //console.log(this.opinionData);
    },
  },
};
</script>