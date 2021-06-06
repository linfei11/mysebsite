<template>
  <el-container class="home-container">
    <el-header>
      <div>
        <span>规则展示系统</span>
      </div>
      <el-button type="info">退出</el-button>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <!--侧边栏菜单区域-->
        <el-menu
          background-color="#333744"
          text-color="#fff"
          active-text-color="#ffd04b"
          :default-active="$route.path"
          router
        >
          <!--一级菜单-->
          <el-menu-item index="/visual">
            <i class="el-icon-setting"></i>
            <template #title>数据可视化</template>
          </el-menu-item>
          <el-menu-item index="/">
            <i class="el-icon-setting"></i>
            <template #title>规则搜索</template>
          </el-menu-item>
          <el-submenu>
            <template #title>
              <i class="el-icon-setting"></i>
              <span>规则添加</span>
            </template>
            <el-submenu index="">
              <template #title>Suricata/snort规则</template>
              <el-menu-item index="/create">
              <template #title>单条规则导入</template>
            </el-menu-item>
                <el-menu-item index="/filecreate">
              <template #title>文件规则导入</template>
            </el-menu-item>
            </el-submenu>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <!--main-->
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<style lang="less" scoped>
.el-header {
  background-color: #333744;
  color: #fff;
  line-height: 60px;
  font-size: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  > div {
    display: flex;
    align-items: center;
  }
}

.el-aside {
  background-color: #333744;
}

.home-container {
  height: 100%;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
}
</style>
