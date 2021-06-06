<template>
  <el-card style="width: 100%">
    <el-row>
      <el-col :span="2"> 按时间搜索 </el-col>
      <el-col :span="6">
        <el-date-picker
          v-model="sTime"
          type="datetimerange"
          align="left"
          unlink-panels
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
          value-format="YYYY-mm-dd HH:MM:SS"
        >
        </el-date-picker>
      </el-col>
      <el-col :span="2">
        <el-button @click="sendSTime" type="success" plain>查询</el-button>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <el-row>
      <el-col :span="2"> 按条件搜索 </el-col>
      <el-col :span="2">
        <el-form label-position="top">
          <el-form-item label="风险等级" size="medium">
            <el-select
              placeholder="请选择风险等级"
              multiple
              collapse-tags
              v-model="risklevel_list"
            >
              <el-checkbox v-model="checkedThing1" @change="selectAllThing1"
                >全选</el-checkbox
              >
              <el-option
                v-for="(item, index) in risklevel_lists"
                :label="item.label"
                :value="item.value"
                :key="index"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="2">
        <el-form label-position="top">
          <el-form-item label="导入类型" size="medium">
            <el-select
              placeholder="请选择导入类型"
              multiple
              collapse-tags
              v-model="input_type_list"
            >
              <el-checkbox v-model="checkedThing2" @change="selectAllThing2"
                >全选</el-checkbox
              >
              <el-option
                v-for="(item, index) in input_type_lists"
                :label="item.label"
                :value="item.value"
                :key="index"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="2">
        <el-form label-position="top">
          <el-form-item label="规则类型" size="medium">
            <el-select
              placeholder="请选择规则类型"
              multiple
              collapse-tags
              v-model="rule_type_list"
            >
              <el-checkbox v-model="checkedThing3" @change="selectAllThing3"
                >全选</el-checkbox
              >
              <el-option
                v-for="(item, index) in rule_type_lists"
                :label="item.label"
                :value="item.value"
                :key="index"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="2">
        <el-button @click="sendCondition" type="success" plain
          >联合查询</el-button
        >
      </el-col>
    </el-row>
  </el-card>
  <el-card>
  <el-table
    :data="attacklist.slice((cur_page - 1) * pageSize, cur_page * pageSize)"
    :row-class-name="tableRowClassName"
    @sort-change="changeSort"
    style="width: 100%"
  >
    <el-table-column label="时间" prop="update_time" sortable></el-table-column>
    <el-table-column
      label="规则等级"
      :formatter="riskFormat"
      prop="risk_level"
      sortable
    >
    </el-table-column>
    <el-table-column label="规则类型" :formatter="typeFormat">
    </el-table-column>
    <el-table-column label="导入类型" :formatter="inputFormat">
    </el-table-column>
    <el-table-column label="规则名" prop="rule_name" sortable>
    </el-table-column>
    <el-table-column label="规则详情" prop="content" show-overflow-tooltip>
    </el-table-column>
    <el-table-column align="center" label="操作">
      <template #default="scope">
        <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
          >编辑</el-button
        >
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)"
          >删除</el-button
        >
        <el-button
          size="mini"
          :disabled="scope.row.pcap_path == null ? true : false"
          @click="handleDownload(scope.$index, scope.row)"
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
    layout="total, sizes, prev, pager, next, jumper"
    :page-size="pageSize"
    :total="totalPages"
  >
  </el-pagination>
  <el-dialog title="修改规则信息" v-model="dialogVisible" width="50%">
    <span>
      <Create :create_form="editForm"></Create>
    </span>
  </el-dialog>
    </el-card>
</template>

<script>
import Create from "../components/Update.vue";
import moment from "moment";
export default {
  components: { Create },
  data() {
    return {
      dialogVisible: false,
      editForm: {},
      attacklist: [],
      search: "",
      cur_page: 1,
      pageSize: 10,
      sTime: [],
      totalPages: 1,
      risklevel_lists: [
        { value: 0, label: "无风险" },
        { value: 1, label: "一般" },
        { value: 2, label: "关注" },
        { value: 3, label: "严重" },
        { value: 4, label: "紧急" },
      ],
      risklevel_list: [],
      checkedThing1: false,
      checkedThing2: false,
      checkedThing3: false,
      input_type_lists: [
        { value: 1, label: "批量导入" },
        { value: 2, label: "手动添加" },
        { value: 3, label: "自动收集" },
      ],
      input_type_list: [],
      rule_type_list: [],
      rule_type_lists: [
        { value: "Trojan", label: "普通木马" },
        { value: "QM_Trojan", label: "QM木马" },
        { value: "Exploit", label: "漏洞利用" },
        { value: "Black_IP", label: "恶意IP" },
        { value: "Black_Domain", label: "恶意域名" },
        { value: "Black_URL", label: "恶意URL" },
        { value: "Black_Mail", label: "恶意邮箱" },
      ],
    };
  },
  mounted() {
    this.getAttackList();
  },
  methods: {
    handleDownload(index, row) {
      this.axios({
        url: "attacks/" + row.id + "/download/",
        method: "get",
        responseType: "blob",
      }).then((res) => {
        if (res.status !== 200) return this.$message.error("error");
        console.log(res);
        this.download(res, row.pcap_path);
      });
    },
    download(res, pcap_path) {
      pcap_path = pcap_path.substr(pcap_path.lastIndexOf("/") + 1);
      //console.log(pcap_path.split('.')[0])
      if ("download" in document.createElement("a")) {
        //支持a标签download的浏览器
        let url = window.URL.createObjectURL(res.data); //为文件流创建构建下载链接
        let link = document.createElement("a"); //创建a标签
        link.style.display = "none";
        link.href = url;
        link.setAttribute("download", pcap_path); //设置a标签的下载动作和下载文件名
        document.body.appendChild(link);
        link.click(); //执行下载
        document.body.removeChild(link); //释放标签
      } else {
        //其他浏览器
        navigator.msSaveBlob(res.data, pcap_path);
      }
    },
    getAttackList() {
      this.axios({
        url: "attacks/?format=json",
        method: "get",
      }).then((res) => {
        if (res.status !== 200) return this.$message.error("error");
        this.transformUpdateTime(res);
      });
    },
    transformUpdateTime(res) {
      this.attacklist = res.data;
      this.totalPages = this.attacklist.length;
      this.attacklist.map((item) => {
        item.update_time = moment(item.update_time).format(
          "YYYY-MM-DD HH:mm:ss"
        );
      });
    },
    handleEdit(index, row) {
      this.axios({
        url: "attacks/" + row.id + "/",
        method: "get",
      })
        .then((res) => {
          if (res.status == 200) {
            this.editForm = res.data;
            this.dialogVisible = true;
            console.log(this.editForm);
          }
        })
        .catch((error) => {
          return this.$message.error("查询规则信息失败");
        });
    },
    handleDelete(index, row) {
      this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.axios({
            url: "attacks/" + row.id + "/",
            method: "delete",
          })
            .then((res) => {
              if (res.status == 204) {
                this.$message({
                  type: "success",
                  message: "删除成功!",
                });
              }
            })
            .catch((error) => {
              return this.$message.error("文件已被删除，请刷新页面");
            });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
    handleCurrentChange(val) {
      this.cur_page = val;
    },
    handleSizeChange(val) {
      this.pageSize = val;
    },
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
    inputFormat(row) {
      if (row.input_type === 1) {
        return "批量导入";
      } else if (row.input_type === 2) {
        return "手动添加";
      } else if (row.input_type === 3) {
        return "自动收集";
      }
    },
    changeSort(val) {
      var fieldName = val.prop;
      var sortingType = val.order;
      if (fieldName == "update_time") {
        this.attacklist.map((item) => {
          item.update_time = moment(item.update_time).valueOf();
        });
        if (sortingType == "descending") {
          this.attacklist = this.attacklist.sort(
            (a, b) => b[fieldName] - a[fieldName]
          );
        } else {
          this.attacklist = this.attacklist.sort(
            (a, b) => a[fieldName] - b[fieldName]
          );
        }
      }
      this.attacklist.map((item) => {item.update_time = moment(item.update_time).format("YYYY-MM-DD HH:mm:ss")})
    },
    sendSTime() {
      this.axios({
        url: "attacks/search1/",
        method: "get",
        params: {
          st_time: this.sTime[0],
          en_time: this.sTime[1],
        },
      }).then((res) => {
        if (res.status !== 200) return this.$message.error("seach error");
        this.transformUpdateTime(res);
      });
    },
    selectAllThing(arra, arras, checkedThing) {
      if (checkedThing) {
        arras.map((item) => {
          arra.push(item.value);
        });
      } else {
        arra = [];
      }
      console.log(arra);
    },
    selectAllThing1() {
      this.risklevel_list = [];
      this.selectAllThing(
        this.risklevel_list,
        this.risklevel_lists,
        this.checkedThing1
      );
    },
    selectAllThing2() {
      this.input_type_list = [];
      this.selectAllThing(
        this.input_type_list,
        this.input_type_lists,
        this.checkedThing2
      );
    },
    selectAllThing3() {
      this.rule_type_list = [];
      this.selectAllThing(
        this.rule_type_list,
        this.rule_type_lists,
        this.checkedThing3
      );
    },
    sendCondition() {
      if (
        (this.risklevel_list.length != 0) &
        (this.input_type_list.length != 0) &
        (this.rule_type_list.length != 0)
      ) {
        this.axios({
          url: "attacks/search1/",
          method: "get",
          params: {
            risk: JSON.stringify(this.risklevel_list),
            in_type: JSON.stringify(this.input_type_list),
            ru_type: JSON.stringify(this.rule_type_list),
          },
        }).then((res) => {
          if (res.status !== 200) return this.$message.error("search error");
          this.transformUpdateTime(res);
        });
      } else {
        this.$alert("有未选复选框", "提示", {
          confirmButtonText: "确定",
        });
      }
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
.el-select .el-input {
  width: 130px;
}
</style>
