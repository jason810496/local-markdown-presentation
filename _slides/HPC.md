# HPC ✖️ AI

---

## 第八組 🛞

---


## AI 應用專題

---

## Task1

`任務：`
GPU 數量與 Performance 的關係

----

### Strong Scalability Chart

![](https://hackmd.io/_uploads/rJMwOMZnh.png)

----

## Task2

`任務：`
在盡可能短的時間把 module 練的盡可能準確


----


### Tuning

* constant learning rate
* auto find batch size 
* 4 epoches

----

### constant learning rate

一開始先調整 learning rate

- `5e-5` -> `1e-4` -> `3e-4` -> `5e-4`

- 最後用 `5e-4`

----


訓練次數用 4 個 epoches

最後可以把 lost 降低到低於 3

```
***** train metrics *****
epoch                    =        4.0
train_loss               =     2.9382
train_runtime            = 0:02:12.84
train_samples            =       2318
train_samples_per_second =     69.797
train_steps_per_second   =      2.198
```



---

## GROMACS 應用專題

----

- 先用預設的 
- 按照用 PPT 先去優化 PME

----

- 用 GPU 去算 PME 
- 然後再多幾顆 GPU 去算，但也沒有比較快

<!-- ( 把 PME 調成 GPU ，發現有提升 ) -->

----

### Profiling

![](https://hackmd.io/_uploads/Bk3nwz-22.png)


我們的成果 👆

---

## HPL&HPCG Benchmark

----

那時後怪怪，所以就跑預設的😓


---

## 營隊學習

----

### CPU / GPU Optimization

- CPU 
    - OMP
    - MPI
- GPU
    - ACC
    - CUDA

----

### OMP & MPI & ACC & CUDA

<br>
這些是我們比較有興趣的！ <br>
<!-- 也比較有寫到程式的感覺 -->
尤其是 MPI 🔥

----

### MPI Load Balancing
- Master-Slave Process

```cpp=
// Master process
while (work_counter < max_work) {
    int available_slave;
    MPI_Status status;
    MPI_Recv(&available_slave, 1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
    if (status.MPI_TAG == WORK_TAG) {
        // Assign work to the available slave
        MPI_Send(&work_counter, 1, MPI_INT, available_slave, WORK_TAG, MPI_COMM_WORLD);
        work_counter++;
    }
}
```

----

- Slave Process
```cpp-
// Slave Process
while (1) {
    MPI_Send(&rank, 1, MPI_INT, 0, WORK_TAG, MPI_COMM_WORLD);
    MPI_Status status;
    int work;
    MPI_Recv(&work, 1, MPI_INT, 0, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
    if (status.MPI_TAG == TERMINATE_TAG) {
        break;
    }
    // Do the assigned work
    printf("Slave %d is working on task %d\n", rank, work);
}
```

----

### ACC
- tailing
![](https://hackmd.io/_uploads/Bky4-wW23.png)


----

比較可惜的是 
在昨天的競賽都沒有用到 <br>
<!-- 單純調參數等結果比較無趣一點 -->


---

## 團隊分工&互助 🤝

----

### 發揮 Parallel 的精神 🥓
<br>

把 Task 切割分 Process 處理 
<br>
- PA , PB ➡️ Task 1
- PC , PD ➡️ Task 2

---

## 生活經驗 👀

----

### 小吃部燒肉飯好好ㄔ🤤


| ![](https://hackmd.io/_uploads/Sytwpebhh.jpg) | ![](https://hackmd.io/_uploads/HJ7h6ebhh.jpg) | ![](https://hackmd.io/_uploads/ByAdalb2h.jpg) |
| -------- | -------- | -------- |

----

### oloo 滑板車好好玩🚀



|   ![](https://hackmd.io/_uploads/S1P7D8W33.jpg) |     ![](https://hackmd.io/_uploads/BydNvUZhn.jpg) |
| --- | --- |


----

### 白鬍子牛排🥩

|   ![](https://hackmd.io/_uploads/HkvtPUW2n.jpg) | ![](https://hackmd.io/_uploads/H139wI-nn.jpg) |
| --- | --- |

---

# HPC AI Camp
## 優質 （很硬🪨）





