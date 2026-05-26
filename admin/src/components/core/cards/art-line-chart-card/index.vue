<template>
  <div
    class="art-card p-5 flex flex-col"
    :class="isNewStyle ? 'h-full' : ''"
    :style="isNewStyle ? {} : { height: `${height}rem` }"
  >
    <template v-if="isNewStyle">
      <div class="pb-3.5">
        <p class="text-lg font-medium">{{ title }}</p>
      </div>
    </template>
    <template v-else>
      <div class="mb-2.5 flex-b items-start">
        <div>
          <p class="text-2xl font-medium leading-none">
            {{ value }}
          </p>
          <p class="mt-1 text-sm text-g-500">{{ label }}</p>
        </div>
        <div
          class="text-sm font-medium"
          :class="[
            percentage > 0 ? 'text-success' : 'text-danger',
            isMiniChart ? 'absolute bottom-5' : ''
          ]"
        >
          {{ percentage > 0 ? '+' : '' }}{{ percentage }}%
        </div>
        <div v-if="date" class="absolute bottom-5 right-5 text-xs text-g-500">
          {{ date }}
        </div>
      </div>
    </template>
    <div
      ref="chartRef"
      class="w-full"
      :class="isNewStyle ? 'flex-1 min-h-0' : ''"
      :style="isNewStyle ? {} : { height: `calc(${height}rem - 5rem)` }"
    ></div>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue'
  import { graphic, type EChartsOption } from '@/plugins/echarts'
  import { getCssVar, hexToRgba } from '@/utils/ui'
  import { useChartOps, useChartComponent, useChart } from '@/hooks/core/useChart'

  defineOptions({ name: 'ArtLineChartCard' })

  interface Props {
    title?: string
    value?: number
    label?: string
    percentage?: number
    date?: string
    height?: number
    color?: string
    showAreaColor?: boolean
    chartData: number[]
    isMiniChart?: boolean
    xAxisData?: string[]
  }

  const props = withDefaults(defineProps<Props>(), {
    height: 11
  })

  const isNewStyle = computed(() => !!props.title)

  const {
    getAxisLineStyle,
    getAxisLabelStyle,
    getAxisTickStyle,
    getSplitLineStyle,
    getTooltipStyle,
    getGridWithLegend
  } = useChart()

  const { chartRef } = useChartComponent({
    props: {
      loading: false
    },
    checkEmpty: () => !props.chartData?.length,
    watchSources: [() => props.chartData, () => props.color, () => props.showAreaColor],
    generateOptions: (): EChartsOption => {
      const computedColor = props.color || useChartOps().themeColor
      const weekDays = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

      return {
        grid: getGridWithLegend(false, 'bottom', {
          top: isNewStyle ? 12 : 0,
          right: 15,
          bottom: 20,
          left: 0
        }),
        tooltip: getTooltipStyle('axis'),
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: props.xAxisData && props.xAxisData.length > 0
            ? props.xAxisData
            : weekDays.slice(0, props.chartData.length),
          axisTick: getAxisTickStyle(),
          axisLine: getAxisLineStyle(true),
          axisLabel: getAxisLabelStyle(true)
        },
        yAxis: {
          type: 'value',
          min: 0,
          axisLabel: getAxisLabelStyle(true),
          axisLine: getAxisLineStyle(false),
          splitLine: props.isMiniChart
            ? { show: false }
            : getSplitLineStyle(true)
        },
        series: [
          {
            data: props.chartData,
            type: 'line',
            smooth: true,
            showSymbol: true,
            symbol: 'circle',
            symbolSize: 6,
            lineStyle: {
              width: 2.5,
              color: computedColor
            },
            areaStyle: props.showAreaColor
              ? {
                  color: new graphic.LinearGradient(0, 0, 0, 1, [
                    {
                      offset: 0,
                      color: props.color
                        ? hexToRgba(props.color, 0.2).rgba
                        : hexToRgba(getCssVar('--el-color-primary'), 0.2).rgba
                    },
                    {
                      offset: 1,
                      color: props.color
                        ? hexToRgba(props.color, 0.01).rgba
                        : hexToRgba(getCssVar('--el-color-primary'), 0.01).rgba
                    }
                  ])
                }
              : undefined,
            emphasis: {
              focus: 'series',
              lineStyle: {
                width: 3.5
              }
            }
          }
        ]
      }
    }
  })
</script>
