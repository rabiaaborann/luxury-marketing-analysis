import plotly.express as px
import plotly.graph_objects as go

class LuxuryVisualizer:
    """
    High-end visualization engine for Luxury Brand Equity and Performance.
    Focuses on clarity, aesthetics, and strategic insights.
    """

    def __init__(self, template="plotly_white"):
        self.template = template
        self.brand_colors = {'Jacquemus': '#FF5733', 'Hermès': '#2E4053'}

    def plot_exclusivity_matrix(self, report_df):
        """
        Creates a 2D Strategy Map: Mean Engagement vs. Exclusivity Score.
        Helps executives identify 'Trend Chasers' vs. 'Heritage Icons'.
        """
        fig = px.scatter(
            report_df,
            x="mean_engagement",
            y="exclusivity_score",
            text="brand",
            size="exclusivity_score",
            color="brand",
            color_discrete_map=self.brand_colors,
            title="Strategic Luxury Positioning: Engagement vs. Exclusivity",
            labels={
                "mean_engagement": "Market Presence (Mean Engagement %)",
                "exclusivity_score": "Exclusivity Stability Score (ESS)"
            }
        )

        fig.update_traces(textposition='top center')
        fig.update_layout(
            template=self.template,
            height=600,
            showlegend=False
        )
        
        return fig

    def plot_volatility_trend(self, original_df):
        """Creates a professional line chart with customized luxury styling."""
        fig = px.line(
            original_df, 
            x='Month', 
            y='Engagement Rate (%)', 
            color='Brand',
            title='Luxury Engagement Volatility Trend',
            line_shape='spline',
            render_mode='svg',
            color_discrete_map=self.brand_colors
        )
        
        fig.update_layout(template=self.template, hovermode='x unified')
        return fig