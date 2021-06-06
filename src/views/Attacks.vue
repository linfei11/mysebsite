<template>
  <el-table
    :data="attacklist.slice((cur_page - 1) * pageSize, cur_page * pageSize)"
    :row-class-name="tableRowClassName"
    :default-sort="{prop: 'update_time', order:'descending'}"
    style="width: 100%"
  >
    <el-table-column label="时间" :formatter="timeFormat" prop="update_time" sortable></el-table-column>
    <el-table-column label="规则等级" :formatter="riskFormat" prop="risk_level" sortable>
    </el-table-column>
    <el-table-column label="规则类型" :formatter="typeFormat">
    </el-table-column>
    <el-table-column label="规则名" prop="rule_name" sortable> </el-table-column>
    <el-table-column label="规则详情" prop="content"> </el-table-column>
    <el-table-column align="right">
      <template #header>
        <el-input v-model="search" size="mini" placeholder="输入关键字搜索" />
      </template>
      <template #default="scope">
        <el-button size="mini" @click="handleDownload(scope.$index, scope.row)"
          >下载</el-button
        >
      </template>
    </el-table-column>
  </el-table>
  <el-pagination
    background
    @current-change="handleCurrentChange"
    @size-change="handleSizeChange"
    :current-page="cur_page"
    layout="prev, pager, next"
    :page-size="pageSize"
    :total="1000"
  >
  </el-pagination>
</template>

<script>
export default {
  data() {
    return {
      attacklist: [],
      search: "",
      pageSize: 10,
      cur_page: 1,
    };
  },
  mounted() {
    this.getAttackList();
  },
  methods: {
    getAttackList() {
      this.axios({
        url: "attacks/?format=json",
        method: "get",
      }).then((res) => {
        if (res.status !== 200) return this.$message.error("error");
        this.attacklist = res.data;
      });
    },
    handleDownload (index, row) {
      console.log(index, row)
    },
    handleCurrentChange(val) {
      this.cur_page = val;
    },
    handleSizeChange() {},
    tableRowClassName({ row, rowIndex }) {
      if (row.risk_level === 0) {
        return "norisk-row";
      } else if (row.risk_level === 1 || row.risk_level === 2) {
        return "normalrisk-row";
      }
      return "serious-row";
    },
    riskFormat(row) {
      if (row.risk_level === 0) {
        return "无风险";
      } else if (row.risk_level === 1) {
        return "一般";
      } else if (row.risk_level === 2) {
        return "关注";
      } else if (row.risk_level === 3) {
        return "严重";
      }
      return "紧急";
    },
    typeFormat(row) {
      if (row.rule_type === "Trojan") {
        return "普通木马";
      } else if (row.rule_type === "QM_Trojan") {
        return "QM木马";
      } else if (row.rule_type === "Exploit") {
        return "漏洞利用";
      } else if (row.rule_type === "Black_IP") {
        return "恶意IP";
      } else if (row.rule_type === "Black_Domain") {
        return "恶意域名";
      } else if (row.rule_type === "Black_URL") {
        return "恶意URL";
      } else if (row.rule_type === "Black_Mail") {
        return "恶意邮箱";
      }
      return "";
    },
    dateFormat(fmt, date) {
      let ret = "";
      date = new Date(date);
      const opt = {
        "Y+": date.getFullYear().toString(), // 年
        "m+": (date.getMonth() + 1).toString(), // 月
        "d+": date.getDate().toString(), // 日
        "H+": date.getHours().toString(), // 时
        "M+": date.getMinutes().toString(), // 分
        "S+": date.getSeconds().toString(), // 秒
      };
      for (let k in opt) {
        ret = new RegExp("(" + k + ")").exec(fmt);
        if (ret) {
          fmt = fmt.replace(
            ret[1],
            ret[1].length == 1 ? opt[k] : opt[k].padStart(ret[1].length, "0")
          );
        }
      }
      return fmt;
    },
    timeFormat(row) {
      return this.dateFormat("YYYY-mm-dd HH:MM", row.update_time);
    },
  },
};
</script>

<style lang="less">
.el-table .norisk-row {
  background: #aaaaaa;
}

.el-table .normalrisk-row {
  background: #ffff66;
}

.el-table .serious-row {
  background: rgb(228, 144, 179);
}
</style>

