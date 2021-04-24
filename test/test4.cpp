#include<stdio.h>
#define MAX_VERTECX_NUM 20
#define INT_MIN 0
int n;
int Path[MAX_VERTECX_NUM][MAX_VERTECX_NUM];
float value[MAX_VERTECX_NUM][MAX_VERTECX_NUM];
typedef struct{
        int vexs[MAX_VERTECX_NUM]; //顶点向量 可以存储每个顶点的信息
        float arc[MAX_VERTECX_NUM][MAX_VERTECX_NUM];//邻接矩阵 主要存放关于边的信息
        int vexnum,arcnum;         //图中当前顶点数和弧数
   }MGraph;
void CreateDG(MGraph *G){
     int i,j,k;
     float w;
     scanf("%d%d",&(G->vexnum),&(G->arcnum));
     printf("G->vexnum=%d,G->arcnum=%d\n",G->vexnum,G->arcnum);
     for(i=1;i<=G->vexnum;i++)
     {
          G->vexs[i]=i;
          }
     for(i=1;i<=G->vexnum;i++)
     {
          for(j=1;j<=G->vexnum;j++)
          {
               G->arc[i][j]=INT_MIN;
               }
          }
     for(k=1;k<=G->arcnum;k++)
     {
          scanf("%d%d%f",&i,&j,&w);
          G->arc[i][j]=w;
          }
     }       
void ShortestPath_FLOYD(MGraph *G)
{
    int i,j,k;
    for(i=1;i<=G->vexnum;i++){
        for(j=1;j<=G->vexnum;j++){
            if(i==j)
                value[i][j]=1;
            else
                value[i][j]=G->arc[i][j];
            if(G->arc[i][j]>INT_MIN)
                Path[i][j]=i;
            else
                Path[i][j]=0;                    
            }
        }
    for(k=1;k<=G->vexnum;k++){
        for(i=1;i<=G->vexnum;i++){
            for(j=1;j<=G->vexnum;j++){            
                  if(value[i][k]*value[k][j]>value[i][j]){
                    value[i][j]=value[i][k]*value[k][j];
                    Path[i][j]=Path[k][j];
                    }                     
                }
            }
        }
     }
void Procedure_print(int i,int j)
{
    if(Path[i][j]==i)
    {
            printf("%d",i);       
            return;
    }
    else if(Path[i][j]==0)//输出结点i与结点j之间不存在通路
        printf("NO path");
    else{
        printf("%d ",Path[i][j]);   
        Procedure_print(i,Path[i][j]);
        }
    }
int main()
{
    int i,j;
    MGraph G;
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    CreateDG(&G);
    ShortestPath_FLOYD(&G);
    i=1;                     
    if(value[i][i]>1)
    {
          printf("%f ",value[i][i]);          
          if(Path[i][i]!=0)
              printf("%d%d ",i,i);
          printf("兑换顺序的逆序输出：%d ",i);
          Procedure_print(i,i);  
          printf("\n");          
     }
}
