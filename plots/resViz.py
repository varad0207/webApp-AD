import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix, classification_report

from io import BytesIO
import base64

class Gen_Plot():
    def __init__(self) -> None:
        pass

    def gen_auc_plot(self, res_dic):
        fig, ax = plt.subplots(figsize=(12, 8), dpi=100)
        ax.plot(res_dic['fpr'], res_dic['tpr'], label=f"AUC = {res_dic['auc_roc']:.4f}", color='royalblue')
        ax.set_xlabel('False Positive Rate', fontsize=14, labelpad=15)
        ax.set_ylabel('True Positive Rate', fontsize=14, labelpad=15)
        ax.set_title('Receiver Operating Characteristic (ROC) Curve', fontsize=16, pad=20)
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15))

        buf = BytesIO()  
        fig.savefig(buf, format="png", bbox_inches='tight')
        plot = base64.b64encode(buf.getbuffer()).decode("ascii") 
        return plot

    def gen_confusion_matrix(self, res_dic):
        fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

        cf_matrix = confusion_matrix(res_dic['y_true'], res_dic['y_pred'])
        sns.heatmap(cf_matrix, annot=True, cmap='Blues', fmt='d', cbar=False, ax=ax)
        ax.set_title('Confusion Matrix', fontsize=16, pad=20)
        ax.set_xlabel('Predicted', fontsize=14, labelpad=15)
        ax.xaxis.set_ticklabels(['Positive', 'Negative'])
        ax.set_ylabel('Actual', fontsize=14, labelpad=15)
        ax.yaxis.set_ticklabels(['Positive', 'Negative'])

        
        buf = BytesIO()  
        fig.savefig(buf, format="png", bbox_inches='tight')
        plot = base64.b64encode(buf.getbuffer()).decode("ascii") 
        return plot
    
    # def gen_classification_report(self, res_dic):
        # report = classification_report(res_dic['y_true'], res_dic['y_pred'])
        # ax3.text(0.5, 0.5, report, fontsize=12, ha='center', va='center', transform=ax3.transAxes, bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))
    
    def comp_auc(self, selected_algo):
        fig, ax = plt.subplots(figsize=(12, 12), dpi=100)

        for model, metric in selected_algo.items():
            ax.plot(metric['fpr'], metric['tpr'], label=f"{model} AUC = {metric['auc_roc']:.4f}")

        ax.set_xlabel('False Positive Rate', fontsize=14, labelpad=15)
        ax.set_ylabel('True Positive Rate', fontsize=14, labelpad=15)
        ax.set_title('Receiver Operating Characteristic (ROC) Curve', fontsize=16, pad=20)
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25))

        buf = BytesIO()  
        fig.savefig(buf, format="png", bbox_inches='tight')
        plot = base64.b64encode(buf.getbuffer()).decode("ascii") 
        return plot